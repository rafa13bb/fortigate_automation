import pyfortiapi
import csv
device = pyfortiapi.FortiGate(ipaddr="",port="",vdom="",username="",password="")
policies = device.get_firewall_policy()
def srcint(current_interface):
    for j in range(len(current_interface)):
        if current_interface[j]['name'] in interfaces:
            return True
            break
        else:
            return False     
                    
header = ["rule ID", "interface origem", "interface destino", "endereço origem", "endereço destino", "portas"]
interfaces = ["list_of_interfaces"] 

############################################### Extração regras com o enderecos "all" #####################################################################
with open("rules_all.csv","w") as s:
       s.write(f'{",".join(header)}\n')
       for i in policies:
            if i['dstaddr']:
                if i['srcaddr'][0]['name'] == 'all' and i['action'] == 'accept' and i['status'] == 'enable' and srcint(i['srcintf']) == True:
                    rule = (str(i['policyid']),  i['srcintf'][0]['name'],  i['dstintf'][0]['name'],  i['srcaddr'][0]['name'],  i['dstaddr'][0]['name'],  i['service'][0]['name'])
                    frase =",".join(rule)
                    s.write(f'{frase}\n')
       for i in policies:
         if i['dstaddr']:
             if i['dstaddr'][0]['name'] == 'all' and i['action'] == 'accept' and i['status'] == 'enable' and srcint(i['dstintf']) == True :
                   rule = (str(i['policyid']),  i['srcintf'][0]['name'],  i['dstintf'][0]['name'],  i['srcaddr'][0]['name'],  i['dstaddr'][0]['name'],  i['service'][0]['name'])
                   frase =",".join(rule)
                   s.write(f'{frase}\n')

############################################## Extração regras com o enderecos "any" #####################################################################                   
with open("rules_any.csv","w") as u:
       u.write(f'{",".join(header)}\n')
       for j in policies:
            if j['srcintf'][0]['name'] == 'any'  and srcint(i['dstintf']) == True:
                   rule2 = (str(j['policyid']),  j['srcintf'][0]['name'],  j['dstintf'][0]['name'],  j['srcaddr'][0]['name'],  j['dstaddr'][0]['name'],  j['service'][0]['name'])
                   frase2 =",".join(rule2)
                   u.write(f'{frase2}\n')
       for j in policies:
            if j['dstintf'][0]['name'] == 'any'  and srcint(i['srcintf']) == True:
                   rule2 = (str(j['policyid']),  j['srcintf'][0]['name'],  j['dstintf'][0]['name'],  j['srcaddr'][0]['name'],  j['dstaddr'][0]['name'],  j['service'][0]['name'])
                   frase2 =",".join(rule2)
                   u.write(f'{frase2}\n')

############################################## Extração regras sem comentarios ############################################################################                  
header1 = ["rule ID"]
with open("rules_no_comments.csv","w") as e:
       e.write(f'{",".join(header1)}\n')
       for i in policies:
            if i['comments'] == '' :
                   rule3 = (str(i['policyid']))
                   e.write(f'{rule3}\n')