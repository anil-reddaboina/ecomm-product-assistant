import importlib.metadata
packages = [
    "beautifulsoup4",
    "fastapi",
    "html5lib",
    "pydantic",
    "requests",
    "selenium",
    "scikit-learn",
    "uvicorn",
    "xgboost",
    "yfinance",
    "pytest",
    "pytest-cov",
    "langchain",
    "langchain-openai",
    "langchain_core" 
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")
