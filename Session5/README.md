# Session 7 Assignment

### def fibonacci(n:'int'):
Generates Fibonacci number given for a range passed in as a parameter.

### def find_fib():
Calls the fibonacci function to check if it generates fibonacci number within a particular range.

### def check_fibonocci(n : 'Number'):
Checks if a number is fibonacci or not

### add_iterables_even_odd
add_iterables_even_odd = lambda iter1,iter2: [x+y for x,y in zip(iter1,iter2) if x%2 == 0 and y%2!=0]

add 2 iterables a and b such that a is even and b is odd

### strip_vowels
strip_vowels = lambda y: ''.join(list(filter(lambda x : x not in "AaEeIiOoUu",y))) strips every vowel from a string provided (tsai>>t s)

### ReLU function for a 1D array
relu_func = lambda x: list(map(lambda y: y if y>0 else 0 ,x))

### a sigmoid function for a 1D array
sigmoid_func = lambda x : list(map(lambda y: (1/(1+math.exp(-y))),x))

#takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn shift_alphabets = lambda input_string : ''.join(map(lambda x: chr(97+(ord(x) - 97)%21 + 5) if ord(x) < 118 else chr(97+(ord(x)-97)%21),filter(lambda x: x in string.ascii_lowercase ,input_string.lower())))

### profanity check
def profanity_check(passage:'string') -> 'checks for validating profanity words': target_url=' https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt' response = requests.get(target_url) checked_list = [i for i in passage.split() if i not in response.text] return bool(checked_list)

### add even number ,find biggest char,add every third number
add_even_no = lambda iterator: reduce(lambda a,b: a+b if b%2==0 else a,iterator,0) #second find_biggest_char = lambda iterator: reduce(lambda a,b: a if ord(a) > ord(b) else b,iterator) #third add_every_third_no = lambda iterator : reduce(lambda a,b: a+b if (iterator.index(b)+1) %3 ==0 else a,iterator,0)

### Generate number plate hardcoded
def generate_number_plate_hardcoded() -> 'generates karnataka number plates': return ['KA' + str(random.randint(10,100)) + random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase) + str(random.randint(1000,10000)) for i in range(15)]

### Generate number plate flexible
def generate_number_plate_flexible(state_code,area_code,alpha_code,reg_no): return state_code + str(area_code) + alpha_code + str(reg_no)

registration_number = partial(generate_number_plate_flexible,area_code = random.randint(10,99),alpha_code = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase), reg_no = random.randint(1000,10000))

### Get number plate
def get_number_plate(state_code): return [registration_number(state_code) for i in range(15)]

