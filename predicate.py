from route_optimization_ny import route_optimisation 

def safe_driving():
    pass

def unsafe_driving(state,message):
    print(f"{message}")


def use_predicate_logic(model_output):
    
    #Getting preloaded message for user error
    output_dict_state= {}
    with open('state_dict.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                output_dict_state[int(key)] = value
    
    

    output_dict_message= {}   

    with open('message_dict.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                output_dict_message[int(key)] = value
    
    
    state=output_dict_state[model_output]
    message=output_dict_message[model_output]
    
    if(model_output in (0,1)):
        safe_driving()
    
    else:
        unsafe_driving(state,message)

#Code start


def get_user_input():
    print("Note: Give location in format - Location, New York")
    start_location=input("Start Location: ")
    end_location=input("End Location: ")

    route_optimisation(start_location,end_location)


if __name__ == '__main__':
    
    model_output=3
    
    
    try:
   
        
        #get_user_input()
        use_predicate_logic(model_output)

    except Exception as e:
        print(f"Error found- {e}")
