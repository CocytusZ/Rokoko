from time import sleep
from pandas import DataFrame
from scapy.all import *
from glove import RkkGlove
from data_analyze import *

'''

'''

# --------------------- Global Config ------------------------#
DATA_INTERVAL = 0.05


# --------------------- Global var def ------------------------#


'''
Global Var
'''
glove = RkkGlove()      # RKK_glove
df = DataFrame(columns=RkkGlove.DATA_HEAD)
cmd = ''                # command use to interact with thread

sniff_filter = "src 192.168.2.119 and udp"

# --------------------- method def start ------------------------#


def callback(packet):
    global glove
    
    # print("Source: %s ===> Dest: %s", packet.src, packet.dst)
    dateStr = time.strftime("%Y_%m%d", time.localtime()) 
    pktdump = PcapWriter("./data/" + dateStr + ".pcap", append=True, sync=True)
    pktdump.write(packet)

    glove.loadData(packet.load)
    # glove.writeCSV()
    glove.writePandas(dataFrame=df)
    print(glove.imu[1].getDataInDecimal()[0])

def sniff_thread_func():
    while True:
        if cmd == 'a':
            sleep(DATA_INTERVAL)
            print('\nPACKAGE CAPTURED:', end='')
            sniff(count=1, filter=sniff_filter, prn=callback)
            # sniff(filter=sniff_filter, prn=callback)

        elif cmd == '':
            # No operation when cmd is default val
            pass
        else:
            print(cmd)
            break


# --------------------- method def end ------------------------#


if __name__ == '__main__':
    save_path = ''
    thread = threading.Thread(target=sniff_thread_func, args=())

    while(True):
        
        cmd = input("New command:")
        if cmd == 'a':
            thread.start()
            print('------------- START COLLECTING DATA -------------')

            
        if cmd == 'b':
            print(df)
            print('------------- Write data frame -------------')

            appendDataFrame('.\csv\data_' + save_path + '.csv', df)
            break
        
        if cmd == 'c':
            print(df)
            print('------------- Append data frame -------------')
            writeDataFrame('.\csv\data_' + save_path + '.csv', df)
            break
        
        if cmd == 'd':
            break

        if cmd == 'e':
            save_path = input('Name the file')
            print('File will saved in \'.\csv\data_\'' + save_path + ' ...')
            print('Press \'c\' to confirm ')
    
        
        if cmd == '0' or cmd == '1' or cmd == '2' or cmd == '3':
            '''
            Mark data:
                0 -> NONE
                1 -> Scissors
                2 -> knife
                3 -> Hammer
            '''
            print(' ------------- Mark data frame -------------')
            time.sleep(2*DATA_INTERVAL)
            # markOneHot(df, cmd, 4)
            save_path = cmd
            cmd = '' # run once only

        
    thread.join()
    print("=============== Sniff End ===============")
