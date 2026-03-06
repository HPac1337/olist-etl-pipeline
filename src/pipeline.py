import logging
from extract import extract
from transform import transform
from load import load

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

def run_pipeline():
    logging.info("Pipeline started.")

    try:
        logging.info("Step 1: Extract")
        data = extract()

        logging.info("Step 2: Transform")
        transformed = transform(data)

        logging.info("Step 3: Load")
        load(transformed)

        logging.info("Pipeline complete.")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()