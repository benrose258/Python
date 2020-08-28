'''
Created on Feb 21, 2017

@author: Ben Rose
'''
blocktokb = 128/1
blocktomb = 1/1024 * blocktokb
blocktogb = 1/1024 * blocktomb
blocktotb = 1/1024 * blocktogb
blocktopb = 1/1024 * blocktotb
blocktoeb = 1/1024 * blocktopb
blocktozb = 1/1024 * blocktoeb
blocktoyb = 1/1024 * blocktozb

blocktobyte = 1024 * blocktokb
blocktobit = 8 * blocktobyte

def blocksToData(blocks,typeofstorage):
    if blocks == 0:
        return str(0) + ' ' + typeofstorage
    else:
        if typeofstorage == 'BIT' or typeofstorage == 'bit':
            return blocks * blocktobit
        elif typeofstorage == 'BYTE' or typeofstorage == 'byte':
            return blocks * blocktobyte
        elif typeofstorage == 'KB' or typeofstorage == 'kb':
            return blocks * blocktokb
        elif typeofstorage == 'MB' or typeofstorage == 'mb':
            return blocks * blocktomb
        elif typeofstorage == 'GB' or typeofstorage == 'gb':
            return blocks * blocktogb
        elif typeofstorage == 'TB' or typeofstorage == 'tb':
            return blocks * blocktotb
        elif typeofstorage == 'PB' or typeofstorage == 'pb':
            return blocks * blocktopb
        elif typeofstorage == 'EB' or typeofstorage == 'eb':
            return blocks * blocktoeb
        elif typeofstorage == 'ZB' or typeofstorage == 'zb':
            return blocks * blocktozb
        elif typeofstorage == 'YB' or typeofstorage == 'yb':
            return blocks * blocktoyb
        else:
            return 'Error: Incorrect input. Please try again.'

def dataToBlocks(data,typeofstorage):
    if data == 0:
        return str(0) + ' ' + typeofstorage
    else:
        if typeofstorage == 'BIT' or typeofstorage == 'bit':
            return data * 1/blocktobit
        elif typeofstorage == 'BYTE' or typeofstorage == 'byte':
            return data * 1/blocktobyte
        elif typeofstorage == 'KB' or typeofstorage == 'kb':
            return data * 1/blocktokb
        elif typeofstorage == 'MB' or typeofstorage == 'mb':
            return data * 1/blocktomb
        elif typeofstorage == 'GB' or typeofstorage == 'gb':
            return data * 1/blocktogb
        elif typeofstorage == 'TB' or typeofstorage == 'tb':
            return data * 1/blocktotb
        elif typeofstorage == 'PB' or typeofstorage == 'pb':
            return data * 1/blocktopb
        elif typeofstorage == 'EB' or typeofstorage == 'eb':
            return data * 1/blocktoeb
        elif typeofstorage == 'ZB' or typeofstorage == 'zb':
            return data * 1/blocktozb
        elif typeofstorage == 'YB' or typeofstorage == 'yb':
            return data * 1/blocktoyb
        else:
            return 'Error: Incorrect input. Please try again.'

print(blocksToData(24457,'gb'))
print()
print(dataToBlocks(2.9854736328125,'gb'))
