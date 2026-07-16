import os
print("LOADING STATUS: Loading programs...")
print("\nChecking dependencies:")

missing: list[str] = []

try:
    import pandas

    print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
except ImportError:
    missing.append("pandas")
    print("[MISSING] pandas")

try:
    import numpy

    print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
except ImportError:
    missing.append("numpy")
    print("[MISSING] numpy")

try:
    import matplotlib
    import matplotlib.pyplot as plt

    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
except ImportError:
    missing.append("matplotlib")
    print("[MISSING] matplotlib")

if missing:
    print(f"\nSome dependencies are missing: {', '.join(missing)}")
    print("\nInstall with pip:")
    print("    pip install -r requirements.txt")
    print("\nInstall with Poetry:")
    print("    poetry install")
else:
    print("\nAnalyzing Matrix data...")
    data = numpy.random.normal(50, 10, 1000)
    print(f"Processing {len(data)} data points...")

    df = pandas.DataFrame({"value": data})
    print(df.describe())

    print("\nGenerating visualization...")
    plt.hist(df["value"], bins=30)
    plt.title("Matrix Data Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")

    print("\nDependency manager comparison:")
    print(f"{'Package':<12}{'Version':<12}{'Managed by'}")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    using_poetry = os.environ.get("POETRY_ACTIVE") == "1" or os.path.exists(os.path.join(script_dir, "poetry.lock"))
    manager = "Poetry (pyproject.toml + poetry.lock)" if using_poetry else "pip (requirements.txt)"

    for pkg_name, pkg_version in [
        ("pandas", pandas.__version__),
        ("numpy", numpy.__version__),
        ("matplotlib", matplotlib.__version__),
    ]:
        print(f"{pkg_name:<12}{pkg_version:<12}{manager}")

    print("\npip installs whatever version range requirements.txt allows,")
    print("without recording an exact resolved version anywhere.")
    print("Poetry resolves every dependency once and pins it in poetry.lock,")
    print("so every teammate gets the exact same versions.")