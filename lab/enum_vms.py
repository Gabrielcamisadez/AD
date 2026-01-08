import ssl
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

ctx = ssl._create_unverified_context()
si = SmartConnect(host="10.5.2.111", user="administrator@telecore.ad", pwd="August1990password", sslContext=ctx)
content = si.RetrieveContent()

for vm in content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True).view:
    ip = vm.guest.ipAddress or (vm.guet.net[0].ipConfig.ipAddress[0].ipAddress if vm.guest.net else "N A")
    print(f"VM: {vm.name}\n Power: {vm.runtime.powerState}\n OS: {vm.config.guestFullName}\n Tools: {vm.guest.toolsStatus}\n")

Disconnect(si)
