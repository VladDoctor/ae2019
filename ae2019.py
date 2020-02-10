import time
import os
import datetime
import random

test_combiner = [[0,5000,50000000],[1,7500,None]]

epoch = 0
max_epoch = 1000000000
max_value = []
min_value = []

def pre_reg(result_arr):
    global max_value
    global min_value

    if (len(max_value) == 0) or (result_arr[0] > max_value[0]):
        max_value = result_arr
    
    if (len(min_value) == 0) or (result_arr[0] < min_value[0]):
        min_value = result_arr


class Simulation(object):
    def __init__(self, data_for_start, data_of_registry):
        if data_of_registry[0] == 0 and data_of_registry[1] == 0:
            pass
        else:
            self.s_reg = Registry()

        self.matrix_dl_bible = {
            '1' :  [0,2,3,2], '2' :  [0,2,3,2], '3' :  [0,2,3,2],
            '4' :  [0,2,3,2], '5' :  [0,2,3,2], '6' :  [0,2,3,2],
            '7' :  [0,2,3,2], '8' :  [0,2,3,2], '9' :  [0,2,3,3],
            '10' : [0,2,3,2], '11' : [0,2,3,2], '12' : [0,2,3,2],
            '13' : [0,2,3,2], '14' : [0,2,3,2], '15' : [0,2,3,2],
            '16' : [0,2,3,2], '17' : [0,2,3,3], '18' : [0,2,3,3],
            '19' : [0,2,3,4], '20' : [0,1,3,6], '21' : [0,0,3,7],
            '22' : [0,2,3,4], '23' : [0,3,3,4], '24' : [0,3,3,3],
            '25' : [0,3,3,3], '26' : [0,3,3,3], '27' : [0,3,3,3],
            '28' : [0,3,3,3], '29' : [0,3,3,3], '30' : [0,3,3,3],
            '31' : [0,3,3,3], '32' : [0,3,3,3], '33' : [0,3,3,3],
            '34' : [1,3,4,3], '35' : [8,3,3,3], '36' : [8,3,3,3],
            '37' : [8,3,3,3], '38' : [8,3,3,3], '39' : [8,3,3,3],
            '40' : [8,3,3,3], '41' : [8,3,3,3], '42' : [8,3,3,3],
            '43' : [8,3,3,3], '44' : [8,3,3,3], '45' : [8,3,3,3],
            '46' : [8,3,3,3], '47' : [8,3,3,3], '48' : [8,3,3,3],
            '49' : [8,3,3,3], '50' : [8,3,3,3], '51' : [8,3,3,3],
            '52' : [8,3,3,3], '53' : [8,3,3,3], '54' : [8,3,3,3]
        }
        
        self.matrix_dl = { 
            '1' :  [2,2,4,2], '2' :  [2,2,3,2], '3' :  [2,2,3,2],
            '4' :  [2,2,3,2], '5' :  [2,2,3,2], '6' :  [2,2,3,2],
            '7' :  [2,2,3,2], '8' :  [2,2,3,2], '9' :  [3,2,3,3],
            '10' : [3,2,3,2], '11' : [3,2,3,2], '12' : [3,2,3,2],
            '13' : [3,2,3,2], '14' : [3,2,3,2], '15' : [3,2,3,2],
            '16' : [3,2,3,2], '17' : [3,2,3,3], '18' : [3,2,3,3],
            '19' : [3,2,3,4], '20' : [3,1,3,6], '21' : [3,0,3,7],
            '22' : [3,2,3,3], '23' : [3,3,3,3], '24' : [3,3,3,3],
            '25' : [3,3,3,3], '26' : [3,3,3,3], '27' : [3,3,3,3],
            '28' : [3,3,3,3], '29' : [3,3,3,3], '30' : [3,3,3,3],
            '31' : [3,3,3,3], '32' : [3,3,3,3], '33' : [3,3,3,3],
            '34' : [3,3,3,3], '35' : [3,3,3,3], '36' : [3,3,3,3],
            '37' : [3,3,3,3], '38' : [3,3,3,3], '39' : [3,3,3,3],
            '40' : [3,3,3,3], '41' : [3,3,3,3], '42' : [3,3,3,3],
            '43' : [3,3,3,3], '44' : [3,3,3,3], '45' : [3,3,3,3],
            '46' : [3,3,3,3], '47' : [3,3,3,3], '48' : [3,3,3,3],
            '49' : [3,3,3,3], '50' : [3,3,3,3], '51' : [3,3,3,3],
            '52' : [3,3,3,3], '53' : [3,3,3,3], '54' : [3,3,3,3]
        }

        self.max_value = []
        self.min_value = []
        
        self.stat = {
            'test_code' : data_for_start[0],
            'years'     : data_for_start[1],
        }
        self.__db_matrix = []
        self.__stat_result = {}
        self.levels = self.__gen_arr_items()
        self.centuries = self.__s_time(self.stat['years'])
        self.data_of_registry = data_of_registry
        
        if self.stat['test_code'] == 0: 
            self.stat['count_of_start'] = data_for_start[2]
            self.stat['flood'] = 0
        elif self.stat['test_code'] == 1:
            self.stat['count_of_start'] = 13
            self.stat['flood'] = 1
        self.__ex_history()

    def __gen_arr_items(self):
        return [[i for i in range(1,7)],
                [i for i in range(8,21)],
                [i for i in range(22,34)],
                [i for i in range(43,45)],
                [i for i in range(120,125)],
                [i for i in range(190,205)],
                [i for i in range(280,285)],
                [i for i in range(100,105)],
                [i for i in range(1,3)]]
        
    def __s_time(self, years):
        data_result = []
        for century in range(1, (years//100) + 1):
            if century > 21:
                data_result.append((century * (-1)) + 21)
            else:
                data_result.append(century)
        data_result.sort()
        return data_result

    def __mdl_index(self, num_oc, dl_param):
        if num_oc < 0 and dl_param == 'd':
            return 0
        elif num_oc > 0 and dl_param == 'd':
            return 1
        elif num_oc < 0 and dl_param == 'b':
            return 2
        elif num_oc > 0 and dl_param == 'b':
            return 3
        else:
            pass

    def __pdl(self, level_od):
        return self.levels[level_od]

    def __gen_stat(self, century):
        def gen_bd(type_of_matrix):
            global b
            global d
            if type_of_matrix == 0:
                b = random.choice(self.levels[self.matrix_dl[str(int((century**2)**0.5))][self.__mdl_index(century, 'b')]])
                d = random.choice(self.levels[self.matrix_dl[str(int((century**2)**0.5))][self.__mdl_index(century, 'd')]])
            elif type_of_matrix == 1:
                b = random.choice(self.levels[self.matrix_dl_bible[str(int((century**2)**0.5))][self.__mdl_index(century, 'b')]])
                d = random.choice(self.levels[self.matrix_dl_bible[str(int((century**2)**0.5))][self.__mdl_index(century, 'd')]])
            
        if self.stat['test_code'] == 0:
            gen_bd(self.stat['test_code'])
        elif self.stat['test_code'] == 1:
            gen_bd(self.stat['test_code'])
        if century > 0:
            while b == d or d > b:
                if self.stat['test_code'] == 0:
                    gen_bd(self.stat['test_code'])
                elif self.stat['test_code'] == 1:
                    gen_bd(self.stat['test_code'])
        else:
            while b == d:
                if self.stat['test_code'] == 0:
                    gen_bd(self.stat['test_code'])
                elif self.stat['test_code'] == 1:
                    gen_bd(self.stat['test_code'])
        self.__db_matrix.append([b,d])
        
    def __ex_history(self):
        for cent in self.centuries:
            if cent == -34 and self.stat['flood'] == 1:
                self.__stat_result['-35'][0] = 8    
            self.__gen_stat(cent)
            
            if len(self.__stat_result.keys()) < 1:
                data_for_ep = self.stat['count_of_start']
            else:
                if cent == 1:
                    data_for_ep = self.__stat_result[str(cent - 2)][0]
                else:
                    keys_of_stat_result = [i for i in self.__stat_result.keys()]
                    if str(cent - 1) == '0':
                        continue
                    else:
                        data_for_ep = self.__stat_result[str(cent - 1)][0]
                pass

            if self.data_of_registry[0] == 1:
                self.s_reg.r_registry(sum([b,d]))
            
            if self.data_of_registry[0] == 1 and self.data_of_registry[1] == 1:
                pass
            else:
                borned = int((data_for_ep * (b/100)))
                death = int((data_for_ep * (d/100)))
                pre_result = data_for_ep - death + borned
            self.__stat_result[str(cent)] = [pre_result, '{0}%'.format(b),'{0}%'.format(d), borned]
        pre_reg([pre_result, self.__db_matrix])

if __name__ == '__main__':
    for test_c in test_combiner:
        start_time = time.time()
        while epoch < max_epoch:
            epoch += 1
            test = Simulation(test_c, [0,0])
        print(str(max_value[0]) + ', ' + str(min_value[0]) + ' - ' + str(time.time() - start_time))
        epoch = 0
        max_value.clear()
        min_value.clear()
