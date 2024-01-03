from TM1py.Services import TM1Service

# pyinstaller main.py --onefile -w

# On-premise BÜTÇE
with TM1Service(address="localhost", port=27401, ssl=True, user="cognos", password="edc*123456",
                namespace="Koctas") as tm1:
    pass

# On-premise IFRS
# with TM1Service(address="localhost", port=51603, ssl=True, user="cognos", password="edc*123456", namespace="Koctas") as tm1:
#     pass

# Migros
# with TM1Service(address="localhost", port=25920, ssl=True, user="cognos", password="Butce2010", namespace="MIGROS") as tm1:
#     pass

# 2023 Demo
# with TM1Service(address="localhost", port=29571, ssl=True, user="admin", password="", namespace="") as tm1:
#     pass

# Cloud Prod
# with TM1Service(
#         base_url='https://catalyst.planning-analytics.cloud.ibm.com/tm1/api/tm1/',
#         user="catalyst01_tm1_automation",
#         namespace="LDAP",
#         password="hXSBg647PJvYs9",
#         ssl=True,
#         verify=True,
#         async_requests_mode=True) as tm1:
#     pass

# Cloud Test
# with TM1Service(
#         base_url='https://catalystest.planning-analytics.cloud.ibm.com/tm1/api/tm1/',
#         user="catalystest01_tm1_automation",
#         namespace="LDAP",
#         password="COorj8U2s4xvMb",
#         ssl=True,
#         verify=True,
#         async_requests_mode=True) as tm1:
#     pass
