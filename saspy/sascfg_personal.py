# SAS ENVIRONMENT
# Change to your SAS environment.
SAS_config_names=['xxxServerNamexxx']

# CONFIGURATION OPTIONS FOR SASPy
# Configuration options for saspy - python Dict   # not required unless changing any of the defaults
# valid key are:
#
# 'lock_down' - True | False. True = Prevent runtime overrides of SAS_Config values below
# 'verbose'   - True | False. True = Allow print statements for debug type messages
# 'prompt'    - True | False. True = Allow prompting as necessary
#
SAS_config_options = {
    'lock_down': False,
    'verbose'  : True,
    'prompt'   : True
    }

# CONFIGURATIONS FOR SAS OUTPUT
# By default output is HTML 5.0 (using "ods html5" statement) but certain templates might not work
# properly with HTML 5.0 so it can also be set to HTML 4.0 instead (using "ods html" statement). This option will only work when using IOM
# in local mode. Note that HTML 4.0 will generate images separately which clutters the workspace and if you download the notebook as HTML,
# the HTML file will need to be put in the same folder as the images for them to appear.
# valid keys are:
#
# 'output' = ['html5', 'html']
# 'style'  = any valid style   # this will be the default for SASsession.HTML_Style, which you can also change dynamically in your code
#
SAS_output_options = {
    'output' : 'html5'
    }

# LOCAL CLASSPATH VARIABLE
# Build out a local classpath variable to use below for Windows clients
#
cpW = "C:\\Program Files\\SASHome\\SASDeploymentManager\\9.4\\products\\deploywiz__94460__prt__xx__sp0__1\\deploywiz\\sas.svc.connection.jar"
cpW += ";C:\\Program Files\\SASHome\\SASDeploymentManager\\9.4\\products\\deploywiz__94460__prt__xx__sp0__1\\deploywiz\\log4j.jar"
cpW += ";C:\\Program Files\\SASHome\\SASDeploymentManager\\9.4\\products\\deploywiz__94460__prt__xx__sp0__1\\deploywiz\\sas.security.sspi.jar"
cpW += ";C:\\Program Files\\SASHome\\SASDeploymentManager\\9.4\\products\\deploywiz__94460__prt__xx__sp0__1\\deploywiz\\sas.core.jar"

# saspyiom.jar
# Change path to the saspyiom.jar where your environment is located.
cpW += ";C:\\xxx\\pythonenv\\Lib\\site-packages\\saspy\\java\\saspyiom.jar"

# CORBA SUPPORT
# These jars provide CORBA support for Java 10+ that no longer provides CORBA itself
#
cpW += ";C:\\xxx\\pythonenv\\Lib\\site-packages\\saspy\\java\\thirdparty\\glassfish-corba-internal-api.jar"
cpW += ";C:\\xxx\\pythonenv\\Lib\\site-packages\\saspy\\java\\thirdparty\\glassfish-corba-omgapi.jar"
cpW += ";C:\\xxx\\pythonenv\\Lib\\site-packages\\saspy\\java\\thirdparty\\glassfish-corba-orb.jar"
cpW += ";C:\\xxx\\pythonenv\\Lib\\site-packages\\saspy\\java\\thirdparty\\pf1-basic.jar"
cpW += ";C:\\xxx\\pythonenv\\Lib\\site-packages\\saspy\\java\\thirdparty\\pf1-tf.jar"

# IOM ENCRYPTION
# Encryption and IOM uses these client side jars
cpW += ";C:\\Program Files\\SASHome\\SASVersionedJarRepository\\eclipse\\plugins\\sas.rutil_904300.0.0.20150204190000_v940m3\\sas.rutil.jar"
cpW += ";C:\\Program Files\\SASHome\\SASVersionedJarRepository\\eclipse\\plugins\\sas.rutil.nls_904300.0.0.20150204190000_v940m3\\sas.rutil.jar"
cpW += ";C:\\Program Files\\SASHome\\SASVersionedJarRepository\\eclipse\\plugins\\sastpj.rutil_6.1.0.0_SAS_20121211183517\\sastpj.rutil.jar"

# WORKSPACE SERVER
# Parameters for selected SAS servers
xxxServerNamexxx = {
    'java': 'java',
    'iomhost': 'xxx', # Change this to the host address
    'iomport': 1234, # Change this to the IOM port
    'encoding': 'latin1',
    'classpath': cpW,
    'authkey': 'IOM_Workspace',
    'sspi': True
    }

