{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "a8f72053-0e2f-4097-905f-28e20375daa5",
     "showTitle": False,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "# test_notebook1.py\n",
    "import pytest\n",
    "from notebooks.notebook1 import add_numbers, subtract_numbers\n",
    "\n",
    "# Test the add_numbers function\n",
    "def test_add_numbers():\n",
    "    # Basic addition\n",
    "    assert add_numbers(3, 2) == 5\n",
    "    # Adding negative numbers\n",
    "    assert add_numbers(-1, 1) == 0\n",
    "    # Adding zeros\n",
    "    assert add_numbers(0, 0) == 0\n",
    "    # Large number addition\n",
    "    assert add_numbers(1000, 2000) == 3000\n",
    "\n",
    "# Test the subtract_numbers function\n",
    "def test_subtract_numbers():\n",
    "    # Basic subtraction\n",
    "    assert subtract_numbers(5, 3) == 2\n",
    "    # Negative result subtraction\n",
    "    assert subtract_numbers(3, 5) == -2\n",
    "    # Subtracting zero\n",
    "    assert subtract_numbers(0, 0) == 0\n",
    "    # Subtraction with larger number first\n",
    "    assert subtract_numbers(10, 5) == 5\n"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "client": "1"
   },
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "test_notebook1.py",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
