import json
import re

d = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''

with open(r"C:\Users\dears002\Documents\adventofcode\input_d19.txt") as f:
    d = f.readlines()
f.close()

d.index('\n')
instructions = d[:d.index('\n')]
parts = d[d.index('\n')+1:]

d = d.split('\n')
instructions = d[0:11]
parts = d[11:]

parts_list = []
for part in parts:
    #part = parts[0]
    part = part.replace('\n', '')
    part = part.replace('=', '":"')
    part = part.replace(',', '","')
    part = part.replace('{', '{"')
    part = part.replace('}', '"}')

    parts_list.append(json.loads(part))

instructions_list = []
for inst in instructions:
    inst = inst.replace('\n', '')
    instructions_list.append(inst)
# inst_dict = {}
# for s in instructions:
#     key = re.search('^[a-z]+', s).group()
#     inst_dict[key] = re.search('{.+}$', s).group()

# for k, v in inst_dict.items():
#     v = v.replace(':', '":"')
#     v = v.replace(',', '","')
#     v = v.replace('{', '{"')
#     v = v.replace('}', '"}')
#     print(v)
#     print(json.loads(v))


def generate_rules(l):
    
    function_names = []
    for s in l:
        name = re.search('^[a-z]+', s).group()
        function_names.append(name)

    rules = []
    for s in l:
        rule = re.search('{.+}$', s).group()
        rule = rule[1:-1].split(',')
        rules.append(rule)
    
    rule_dict = {}
    for i in range(len(function_names)):
        rule_dict[function_names[i]] = rules[i]
    rule_dict

    def f_factory(k, v):
        def f(p):
            print('RULE:', k)
            print('STEPS:', v)
            print('PART SPECS:')
            p.get_specs()
            for step in v:
                try:
                    condition, result = step.split(':')
                    if re.search('>', condition):
                        spec, num = condition.split('>')
                        if getattr(p, spec) > int(num):
                            if result == 'A':
                                print('ACCEPTED')
                                accepted.append(p)
                                break
                            elif result == 'R':
                                print('REJECTED')
                                rejected.append(p)
                                break
                            else:
                                print(result)
                                return result
                    elif re.search('<', condition):
                        spec, num = condition.split('<')
                        if getattr(p, spec) < int(num):
                            if result == 'A':
                                print('ACCEPTED')
                                accepted.append(p)
                                break
                            elif result == 'R':
                                print('REJECTED')
                                rejected.append(p)
                                break
                            else:
                                print(result)
                                return result           
                except ValueError:
                    if step == 'A':
                        print('ACCEPTED')
                        accepted.append(p)
                        break
                    elif step == 'R':
                        print('REJECTED')
                        rejected.append(p)
                        break
                    else:
                        print(step)
                        return step     
        return f
        # def f(p):
        #     print(k)
        #     print(v)
        #     for step in v:
        #         if_then = step.split(':')
        #         if len(if_then) == 2:
        #             print('MAKE IF THEN', str(if_then))
        # return f

    for k, v in rule_dict.items():
        rule_dict[k] = f_factory(k, v)
    
    return rule_dict
    
rule_dictionary = generate_rules(instructions_list)

accepted = []
rejected = []

def analyze_part(part, rule_dictionary, start='in'):
    f = rule_dictionary[start]
    result = f(part)
    if result == None:
        next
    else:
        analyze_part(part, rule_dictionary, start=result)

class Part():

    def __init__(self, specs):
        
        self.x = int(specs['x'])
        self.m = int(specs['m'])
        self.a = int(specs['a'])
        self.s = int(specs['s'])

    def get_specs(self):
        print('x:', self.x, 'm:', self.m, 'a:', self.a, 's:', self.s)
    
    def add_ratings(self):
        return self.x + self.m + self.a + self.s

for part in parts_list:
    print('**************************')
    p = Part(part)
    p.get_specs()
    analyze_part(p, rule_dictionary)

accepted
rejected

rating_total = 0
for part in accepted:
    part.get_specs()
    rating_total += part.add_ratings()
rating_total