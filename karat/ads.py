# https://www.jianshu.com/p/fdbcba5fe5bc

class Solution:
    def adConversationRate(self, cpu_ids, clicks, ips):
        ipmap={}
        total={}
        purchased={}
        cpu_ids=set(cpu_ids)

        for _ in ips:
            id, ip=_.split(',')
            ipmap[ip]=id
        for _ in clicks:
            ip,junk,ad = _.split(',')
            if ad in total:
                initial=int(total[ad])
            else:
                initial=int(0)
                purchased[ad]=0
            total[ad]=int(initial+1)

            if ip in ipmap:
                    purchased[ad]=int(purchased[ad]+1)

        str='' 
        for _ in total:
            str=str+f'{purchased[_]} of {total[_]}  {_}\n'

        return str


completed_purchase_user_ids = ["3123122444","234111110", "8321125440", "99911063"]

# And our ops team provided us with some raw log data from our ad server showing every time a
#user clicked on one of our ads:

 #"IP_Address,Time,Ad_Text"
ad_clicks = [
 "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
 "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
 "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
 "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
 "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
 "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens"]

#The client also sent over the IP addresses of all their users.

all_user_ips = [
"2339985511,122.121.0.155",
 "234111110,122.121.0.1",
 "3123122444,92.130.6.145",
 "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
 "8321125440,82.1.106.8",
 "99911063,92.130.6.144"
 ]

a=Solution()
print (a.adConversationRate(completed_purchase_user_ids,ad_clicks,all_user_ips))