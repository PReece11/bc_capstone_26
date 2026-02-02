from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from bc_capstone_26.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
):
    import pandas as pd

    logger.info(f"Reading raw CSV from: {input_path}")
    df = pd.read_csv(input_path)

    # tiny cleaning step: keep only the first 5 columns
    df = df.iloc[:, :5]

    logger.info(f"Writing processed CSV to: {output_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
