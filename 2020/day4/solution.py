### Day 4: Passport Processing ###

from typing import Optional
from pydantic import BaseModel, ValidationError, validator, constr

required_attrs = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

class PassportModel(BaseModel):
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: constr(regex=r'^#([0-9]|[a-f]){6}$')
    ecl: constr(regex=r'^(amb|blu|brn|gry|grn|hzl|oth)$')
    pid: constr(regex=r'^[0-9]{9}$')
    cid: Optional[str]

    @validator('byr')
    def byr_valid(cls, v):
        if not (len(str(v)) == 4 and 1920 <= int(v) <= 2002):
            raise ValueError()
        return v

    @validator('iyr')
    def iyr_valid(cls, v):
        if not (len(str(v)) == 4 and 2010 <= int(v) <= 2020):
            raise ValueError()
        return v

    @validator('eyr')
    def eyr_valid(cls, v):
        if not (len(str(v)) == 4 and 2020 <= int(v) <= 2030):
            raise ValueError()
        return v

    @validator('hgt')
    def hgt_valid(cls, v):
        unit = v[-2:]
        value = v[:-2]
        if not (unit == 'cm' or unit == 'in'):
            raise ValueError()
        elif unit == 'cm':
            if not (150 <= int(value) <= 193):
                raise ValueError()
        elif unit == 'in':
            if not (59 <= int(value) <= 76):
                raise ValueError()

        return v

def is_passport_valid(passport_dict):
    try:
        PassportModel(**passport_dict)
    except ValidationError as e:
        return False
    return True

def part_1():
    passports = []
    cur_passport = {}
    with open('input.txt', 'r') as input:
        for i, line in enumerate(input):
            line = line.rstrip()
            if not line or line.isspace():
                passports.append(cur_passport)
                cur_passport = {}
            else:
                kv_pairs = line.split(' ')
                for kv_pair in kv_pairs:
                    key, value = kv_pair.split(':')
                    cur_passport[key] = value
        passports.append(cur_passport)
        print(passports)

    total_valid = 0
    for passport in passports:
        if is_passport_valid(passport):
            total_valid += 1

    return total_valid

print(part_1())
# part_1 solution: 210
# part_2 solution: 131
