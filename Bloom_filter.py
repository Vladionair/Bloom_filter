gAAAAABfUd_72rAdCRLDxi9OxYWBfkN466ukf3yGpgkGpXcOZQ3uLz_WJOsgfOYxojQEUCzOSbaUtmm5Gpemc81wCNT9L98zZsVw1L5ygMrA8prVvhYdUPSUmkgg9Llf3KStHRzauBiXEWDBlQM2ZonQtXw3uk7di64EiMYgNLn_Jx0U8bECzetztMWyy4r5Jyy7AOP3IfUR1PCPzstd2NnK1qD0np3XbMsWHuktvoJVpC_TetqsLaXrndrwFxc--NUDwNmccXUEKUrfZPALCwDMEglzdNus01i_U4E4njh5KXL-dcxN4OKOFBInNhjMNeynz6kC37h1DkEyb9Eim6XanvqfDiniC0dui0xrJkP1pElfdoPVRUmjn9lWyrsErTNboJdAxCrzCC_uvMBqjbYwP7pkAc93uKBMT85SKU4AMbi-8SIi-Z6OYwo_L0SNyBf24epArjL5WkZ_uw0RwEGzZdsRfBuXBwJrzAHB-rcrBL22bFl_9iLg-nS1tF5Et_2jTXk94yJNaMmKgP_CgjENgGn-IcwTFpESu6045PNOpVbYbJ5cjYqOhrzlHPZ7V2JQnMJoMm6LCqF8SX6FaUyCFxlfmN7nETQ382xEHyr_hu5YiCI1c5V-gJgiCiz-dFSwLZ1ah4l17HDihbVziQ1uXHfm8z7HSY8gCrBYt0nDj59EGqswMRfsi92mBxo2z2MR979KJhVCuCsLZ-gNlyUc5JpKPS8O7ej0wLXTo2SWRTRhtiGzMbuTqh4X8cQZb_UjfaLs3OtINAmaFPJvm7-itR6X7whsm40nydlQD5uSVG-xXSXsJD3m7LfDTiTcEA0ih4VNaX75Vzu61vWWIph9cajxA3UmEkBLrMIIWHdIEsW4PIcsYFh9rjCmJ8ZerKQEzl8L5r0yw9E5CoSXz67FIr0zD7aufi93JjAioUgNiw0aK4Ghh_6mz7r3IuiQ9rIv6PHnueTxW-pIACeoqc3mLOl8j04yeyJFoSh2F4nS2VdimVJuwUdT9AL15T6TOaKcEanPHIGwbVNpEuaCFa5dCcxMvkWEDMmUktxUGCxAfRtBQOHkTRgbNmEuOkcPbgZu6Bz8_c4JeKdq1aNMLhaR-BfsBBN0D2L_jx0yH4OCNyIFemffQOcF5rsG1IFAYav1MIb-_SDJrrDFpAOB-4oXdPqYuLn-EjOH6GEiuvirjF9mJTABWply_KYPcdGmTSWM_3wfqrCBlDaLXg2zR1HvJhPvY9aj-A==

import bitarray

class BloomFilter:

    def __init__(self, f_len):

        self.filter_len = f_len
        self.bitarray = bitarray(self.filter_len)
        self.bitarray.setall(0)

    def hash1(self, str1):

        sum = 0
        for c in str1:
            code = ord(c)
            sum += code
        return ((sum - ord(str1[0])) * 17) % 32

    def hash2(self, str1):

        sum = 0
        for c in str1:
            code = ord(c)
            sum += code
        return ((sum - ord(str1[0])) * 223) % 32

    def add(self, str1):

        self.bitarray[self.hash1(str1)] = 1
        self.bitarray[self.hash2(str1)] = 1
        return self.bitarray

    def is_value(self, str1):
      
        if self.bitarray[self.hash1(str1)] == 1 and self.bitarray[self.hash2(str1)] == 1:
            return True
        else:
            return False
