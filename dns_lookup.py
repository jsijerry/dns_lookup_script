import os,re,socket

filename = 'lookup_input_file.txt'
input_file = open((os.path.join(os.getcwd(), filename)),'r');
result_file=(os.path.join(os.getcwd(), 'ping_script_result.txt'))

def lookup(ip):
        if(len(str(re.search('[a-zA-Z]',ip))))==4:
                try:
                        print("Performing a reverse lookup of {}".format(ip))
                        website=socket.gethostbyaddr(ip)
                        return("The input {} is an IP address. It belongs to :{} ".format(ip,website[0]))
                except socket.error:
                        print("There was an error in getting the reverse lookup value for {}".format(ip))
                        
        else:
                try:
                    print('\n')
                    print('Trying to find the IP address of {}'.format(ip))
                    dns = socket.gethostbyname(str.strip(ip))
                    return("The IP of {} is - {}".format(ip,dns))
                except socket.error:
                        print("There was an error in getting the DNS lookup value for {}".format(ip))
                        pass

def delete_previous_result():
        try:
                os.remove(result_file)
        except:
                print("Error while deleting file")

delete_previous_result()

for each_host in input_file:
        each_host=str.strip(each_host)
        if str(each_host):
            with open('ping_script_result.txt','a') as result:
                result.write(lookup(each_host))
                result.write("\n")
result.close()
