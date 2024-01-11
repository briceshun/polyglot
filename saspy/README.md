# Python and SAS using SASpy
The SASPy module provides Python APIs to the SAS system. It allows the user to:

* Swap between writing code in Python and SAS (using Jupyter Notebooks).
* Move data between SAS datasets and Pandas dataframes.
* Exchange values between Python variables and SAS macro variables.

**Dependencies**
* Python 3.4 or higher.
* SAS 9.4 or higher. SAS Viya 3.1 or higher is also supported.
* To use the integrated object method (IOM) access method (one of 4 connection methods) requires Java 7 or higher on the client.

---

## Requirements
The `requirements.txt` file contains the 3 main modules required to work with SAS in Python. These modules are:

```python
python -m pip install jupyterlab
python -m pip install SAS-kernel
python -m pip install saspy
```

---

## One-Off Setup
The following files need to be created to set up the SASPy connection.

### Finding IOM Workspace Server details
```sas
* Connection details;
%let host=;
%let port=;
%let userid=;
%let passwrd=;

* Retrieve details;
prom iom operate 
    uri="iom://&host.:&port.;Bridge;USER=&userid.,PASS=&passwrd.";
    list defined filter="- Workspace";
quit;
```

### sascfg_personal.py
The `sascfg_personal.py` file is a configuration file that stipulates the SAS connection parameters using the IOM method. Copy this file into your HOME folder `C:\Users\<userid>\.saspy` and update it with your directories (usually found in the C: drive). The folder is hidden.


The original file this template is based on can be found in the directory the SASPy module is installed. For Anaconda it is in `C:\Program Files\Anaconda3\Lib\site-packages\saspy\sascfg.py`. For Python it will be in your environment's directory.

### Authkey Option
The `"authkey"` option in the `sascfg_personal.py` file allows automatic authentication parameters.
Copy the `_authinfo` file in your HOME directory (`C:\Users\<userid>`). Update the file with your details.