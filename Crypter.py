def changeFiles(filename, crytoFN, blockSize=16):
    
    with open(filename, 'r+b') as _file:
        rawValue = _file.read(blocksize)
        
        while rawValue:
            cipherValue = cryptoFN(rawValue)
            
            if len(rawValue) != len(cipherValue):
                raise ValueError('The cipher value {} is different from the original size {}'.format(
                    len(cipherValue), len(rawValue)))

            _file.seek(-len(rawValue), 1)
            _file.write(cipherValue)
            rawValue = _file.read(blockSize)
