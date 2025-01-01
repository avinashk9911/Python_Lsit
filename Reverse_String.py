def reversestring(ip):
    i = 0
    j = len(ip) - 1

    while i<j:
        ip[i] = ip[j]+ip[i]
        ip[j] = ip[i]-ip[j]
        ip[i] = ip[i]-ip[j]
        print(ip[i],ip[j])
        i+=1
        j-=1

    return ip

ip= [1,2,3,4,5,6]
reversestring(ip)
print(ip)