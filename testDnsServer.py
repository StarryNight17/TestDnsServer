from nslookup import Nslookup
from pythonping import ping
from eventlet.timeout import Timeout

DOMAIN = ['m.jd.com',
          'm.taobao.com',
          'm.weibo.com',
          'm.cmbchina.com',
          'm.ccb.com'
          'www.jd.com',
          'www.taobao.com',
          'www.weibo.com']

DNS_SERVERS=['114.114.114.114',
             '223.5.5.5',
             '223.6.6.6',
             '119.29.29.29',
             '180.76.76.76',
             '202.103.225.68',
             '8.8.8.8']

def test(domain, dns_servers):
    domain_number, best_servers = domain.__len__(), []

    for index, dns in enumerate(dns_servers):
        success_count, avg_ms = 0, 0
        print('---------------------------------')
        print('-------------', dns, '--------------')
        for d in domain:
            dns_query = None
            with Timeout(2, False):
                dns_query = Nslookup(dns_servers=[dns])
                if dns_query is not None:
                    ips_record = dns_query.dns_lookup(d)
                    server, r =  ips_record.answer[0], ping(ips_record.answer[0], timeout=1, size=40, count=10)
                    print(d, '-->', server, 'min: ',r.rtt_min_ms,'max: ',r.rtt_max_ms,'avg: ',r.rtt_avg_ms)
                    avg_ms = avg_ms + r.rtt_max_ms
                    if r.rtt_avg_ms < 300:
                        success_count = success_count + 1


        print('DNS: {}'.format(dns), '\n',
              'Resolving Rate: {:.2f}%'.format(success_count/domain_number*100), '\n',
              'Average Delay: {:.2f}'.format(avg_ms/success_count))
        if success_count == domain_number:
            best_servers.append([dns, avg_ms/success_count])
            print('Best Selected?', 'Yes!')
        else:
            print('Best Selected?', 'No')

    print('----------------Top Rank----------------')
    best_servers.sort(key=lambda x: x[1])
    for item in best_servers: print(item[0], '{:.2f}ms'.format(item[1]))
    print('----------------End Rank----------------')


if __name__ == '__main__':
    test(DOMAIN, DNS_SERVERS)