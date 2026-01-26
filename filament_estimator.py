"""
filament_estimator.py
Minimal Eulerian filament rotation estimators for Phase 1 (GRID backend).

Assumptions:
- All coordinates in Mpc.
- Velocity grid provides v(x,y,z) in km/s (or consistent units), sampled via trilinear interpolation.
- Filament axis is defined by segment endpoints (x0,y0,z0) -> (x1,y1,z1).
"""

from __future__ import annotations
import numpy as np

# ----------------------------
# Utilities
# ----------------------------
def _unit(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v)
    if n == 0:
        raise ValueError("Zero-length vector in _unit()")
    return v / n

def _orthonormal_basis(axis: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Given axis (3,), return (e_par, e1, e2) where:
    - e_par is unit axis
    - e1, e2 span the perpendicular plane
    """
    e_par = _unit(axis.astype(float))
    # Choose a helper vector not parallel to e_par
    a = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(a, e_par)) > 0.9:
        a = np.array([0.0, 1.0, 0.0])
    e1 = _unit(np.cross(e_par, a))
    e2 = _unit(np.cross(e_par, e1))
    return e_par, e1, e2

# ----------------------------
# Velocity grid handling
# ----------------------------
def load_velocity_grid(npz_path: str) -> dict:
    """
    Load a velocity grid from NPZ.

    Supported formats:

    (A) Component format:
        vx, vy, vz  (3D arrays)
        optional: x0, y0, z0, dx

    (B) Packed format (your analytic grid):
        VEL_GRID (nx,ny,nz,3)
        GRID_ORIGIN (3,)  -> x0,y0,z0
        GRID_DX (scalar)  -> dx
    """
    data = np.load(npz_path, allow_pickle=True)
    keys = set(data.files)

    # Case (B): packed velocity grid
    if "VEL_GRID" in keys:
        V = data["VEL_GRID"]
        if V.ndim != 4 or V.shape[-1] != 3:
            raise ValueError(f"VEL_GRID must have shape (nx,ny,nz,3); got {V.shape}")

        grid = {
            "vx": V[..., 0],
            "vy": V[..., 1],
            "vz": V[..., 2],
        }

        if "GRID_ORIGIN" in keys:
            x0, y0, z0 = map(float, data["GRID_ORIGIN"])
            grid["x0"], grid["y0"], grid["z0"] = x0, y0, z0
        if "GRID_DX" in keys:
            grid["dx"] = float(data["GRID_DX"])

        return grid

    # Case (A): component format
    def get_arr(*names):
        for n in names:
            if n in keys:
                return data[n]
        raise KeyError(f"None of keys found: {names}")

    vx = get_arr("vx", "Vx", "velx")
    vy = get_arr("vy", "Vy", "vely")
    vz = get_arr("vz", "Vz", "velz")

    grid = {"vx": vx, "vy": vy, "vz": vz}

    for k in ["x0", "y0", "z0", "dx"]:
        if k in keys:
            grid[k] = float(data[k])

    return grid

    # Case (A): component format
    def get_arr(*names):
        for n in names:
            if n in keys:
                return data[n]
        raise KeyError(f"None of keys found: {names}")

    vx = get_arr("vx", "Vx", "velx")
    vy = get_arr("vy", "Vy", "vely")
    vz = get_arr("vz", "Vz", "velz")

    grid = {"vx": vx, "vy": vy, "vz": vz}

    for k in ["x0", "y0", "z0", "dx"]:
        if k in keys:
            grid[k] = float(data[k])

    return grid

    # Case (A): component format
    def get_arr(*names):
        for n in names:
            if n in keys:
                return data[n]
        raise KeyError(f"None of keys found: {names}")

    vx = get_arr("vx", "Vx", "velx")
    vy = get_arr("vy", "Vy", "vely")
    vz = get_arr("vz", "Vz", "velz")

    grid = {"vx": vx, "vy": vy, "vz": vz}

    for k in ["x0", "y0", "z0", "dx"]:
        if k in keys:
            grid[k] = float(data[k])

    return grid

def trilinear_sample(grid: dict, pos_mpc: np.ndarray) -> np.ndarray:
    """
    Trilinear sample of v(x,y,z) at position pos_mpc (3,).
    Requires grid metadata: x0,y0,z0,dx.
    Returns velocity vector (3,) in same units as grid velocities (e.g. km/s).
    """
    x0 = grid.get("x0", None)
    y0 = grid.get("y0", None)
    z0 = grid.get("z0", None)
    dx = grid.get("dx", None)
    if any(v is None for v in [x0, y0, z0, dx]):
        raise ValueError("Grid missing metadata x0,y0,z0,dx required for sampling.")

    x, y, z = pos_mpc
    fx = (x - x0) / dx
    fy = (y - y0) / dx
    fz = (z - z0) / dx

    i = int(np.floor(fx))
    j = int(np.floor(fy))
    k = int(np.floor(fz))

    # fractional part
    tx = fx - i
    ty = fy - j
    tz = fz - k

    # bounds check
    nx, ny, nz = grid["vx"].shape
    if i < 0 or j < 0 or k < 0 or i+1 >= nx or j+1 >= ny or k+1 >= nz:
        return np.array([np.nan, np.nan, np.nan], dtype=float)

    def lerp(a, b, t): return a*(1-t) + b*t

    v = np.zeros(3, dtype=float)
    for comp, key in enumerate(["vx", "vy", "vz"]):
        A = grid[key]
        c000 = A[i  , j  , k  ]
        c100 = A[i+1, j  , k  ]
        c010 = A[i  , j+1, k  ]
        c110 = A[i+1, j+1, k  ]
        c001 = A[i  , j  , k+1]
        c101 = A[i+1, j  , k+1]
        c011 = A[i  , j+1, k+1]
        c111 = A[i+1, j+1, k+1]

        c00 = lerp(c000, c100, tx)
        c10 = lerp(c010, c110, tx)
        c01 = lerp(c001, c101, tx)
        c11 = lerp(c011, c111, tx)

        c0 = lerp(c00, c10, ty)
        c1 = lerp(c01, c11, ty)

        v[comp] = lerp(c0, c1, tz)

    return v

# ----------------------------
# Ring sampling estimator
# ----------------------------
def ring_mean_vphi(center_mpc: np.ndarray,
                   axis_vec: np.ndarray,
                   R_mpc: float,
                   nphi: int,
                   grid: dict) -> float:
    """
    Sample velocities around a ring of radius R_mpc around the filament axis at 'center_mpc'
    and return mean azimuthal velocity <v_phi>.

    Definition:
      - e_par: unit axis
      - e1,e2: perpendicular basis
      - ring points: center + R*(cosφ e1 + sinφ e2)
      - azimuthal unit vector at φ: e_phi = -sinφ e1 + cosφ e2
      - v_phi(φ) = v · e_phi
    """
    e_par, e1, e2 = _orthonormal_basis(axis_vec)

    phis = np.linspace(0, 2*np.pi, nphi, endpoint=False)
    vphis = []

    for phi in phis:
        offset = R_mpc * (np.cos(phi)*e1 + np.sin(phi)*e2)
        p = center_mpc + offset
        v = trilinear_sample(grid, p)
        if np.any(np.isnan(v)):
            continue
        e_phi = (-np.sin(phi)*e1 + np.cos(phi)*e2)
        vphis.append(float(np.dot(v, e_phi)))

    if len(vphis) == 0:
        return float("nan")
    return float(np.mean(vphis))

def segment_axis_from_row(row) -> np.ndarray:
    p0 = np.array([row["x0"], row["y0"], row["z0"]], dtype=float)
    p1 = np.array([row["x1"], row["y1"], row["z1"]], dtype=float)
    return p1 - p0

def segment_center_from_row(row) -> np.ndarray:
    return np.array([row["cx"], row["cy"], row["cz"]], dtype=float)

def segment_radial_profile(row,
                           R_list_mpc: list[float],
                           nphi: int,
                           grid: dict) -> dict:
    """
    Compute vphi_mean(R) for a single segment (using its center and axis).
    Returns dict with keys like vphi_R1, vphi_R2, ...
    """
    axis = segment_axis_from_row(row)
    c = segment_center_from_row(row)

    out = {}
    for R in R_list_mpc:
        out[f"vphi_R{R}"] = ring_mean_vphi(c, axis, float(R), int(nphi), grid)
    return out
