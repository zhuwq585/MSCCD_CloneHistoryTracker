#####
# this script is used to filter out project clones bewteen drivers from different series of STM chips

import re
def ifSTMDriverPath(path):
    ## check if the path contains substrings like stm32xx, use regular expression to check it 
    stm32DriverPattern = re.compile(r'stm32[a-z0-9][a-z0-9]')
    stm8DriverPattern = re.compile(r'stm8\w')
    
    path = path.lower()
    
    ## check if the path contains substrings like stm32xx, if true, return the matched substring
    stm32DriverMatch = stm32DriverPattern.search(path)
    stm8DriverMatch = stm8DriverPattern.search(path)
    
    if stm32DriverMatch:
        # return stm32DriverMatch.string[0:7]
        return path[stm32DriverMatch.start():stm32DriverMatch.end()]
    elif stm8DriverMatch:
        return path[stm8DriverMatch.start():stm8DriverMatch.end()]
    else:
        return False
    
    
def ifNotSameSTMDriver(path1, path2):
    res1 = ifSTMDriverPath(path1)
    res2 = ifSTMDriverPath(path2)
    
    if not res1 or not res2:
        return True
    else:
        return res1 == res2

if __name__ == "__main__":
    a = ifNotSameSTMDriver("/Users/syu/IoT_Projs/C_C++/AliOS-Things/hardware/chip/stm32u5/drivers/STM32U5xx_HAL_Driver/Src/stm32u5xx_hal_dac_ex.c", "/Users/syu/IoT_Projs/C_C++/mbed-os/targets/TARGET_STM/TARGET_STM32WL/STM32Cube_FW/STM32WLxx_HAL_Driver/stm32wlxx_hal_dac_ex.c")
    print(a)