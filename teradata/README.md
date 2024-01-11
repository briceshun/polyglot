# Python and Teradata using teradatasql and teradataml
The teradatasql and teradataml modules provides Python APIs to the SAS system. It allows the user to:

* Swap between writing code in Python and Teradata (using Jupyter Notebooks).
* Move data between teradata tables and Pandas dataframes.
* Exchange values between Python variables and Teradata variables.

---

## Requirements
The `requirements.txt` file contains the 4 main modules required to work with teradata in Python. These modules are:

```python
python -m pip install ipython-sql
python -m pip install sqlalchemy
python -m pip install teradatasql
python -m pip install teradatasqlalchemy
python -m pip install teradataml
```