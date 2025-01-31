#!/bin/bash

# Activate virtual environment (adjust the path if needed)
source venv/bin/activate

# Run the test suite
echo "Running the test suite..."
pytest --maxfail=1 --disable-warnings -q

# Capture the exit code from pytest
EXIT_CODE=$?

# Check if pytest ran successfully or failed
if [ $EXIT_CODE -eq 0 ]; then
  echo "All tests passed!"
  exit 0
else
  echo "Some tests failed!"
  exit 1
fi

