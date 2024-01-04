#!/usr/bin/env python
# coding: utf-8

# In[1]:


def volume_metrics():
    select_metric=input('Enter the metric of the input: options are "cubic metre", "litre", "gallon", "barrel"')
    output_metric=input('Enter the metric of the wanted output: options are "cubic metre", "litre", "gallon", "barrel"')
    value=int(input('Enter the value of the input: '))
    if select_metric=="cubic metre" and output_metric=="litre":
        return value*1000
    elif select_metric=="cubic metre" and output_metric=="barrel":
        return value*6.289
    elif select_metric=="cubic metre" and output_metric=="gallon":
        return value*264.172
    elif select_metric=="litre" and output_metric=="cubic metre":
        return value*0.001
    elif select_metric=="litre" and output_metric=="barrel":
        return value*0.006
    elif select_metric=="litre" and output_metric=="gallon":
        return value*0.264
    elif select_metric=="barrel" and output_metric=="cubic metre":
        return value*0.158
    elif select_metric=="barrel" and output_metric=="litre":
        return value*158
    elif select_metric=="barrel" and output_metric=="gallon":
        return value*42
    elif select_metric=="gallon" and output_metric=="cubic metre":
        return value*0.0037
    elif select_metric=="gallon" and output_metric=="litre":
        return value*3.785
    elif select_metric=="gallon" and output_metric=="barrel":
        return value*0.0238
    else:
        print("Wrong format")


# In[2]:


volume_metrics()


# In[8]:


def volume_metrics2():
    metric_factors = {
        "cubic metre": {"litre": 1000, "barrel": 6.289, "gallon": 264.172},
        "litre": {"cubic metre": 0.001, "barrel": 0.006, "gallon": 0.264},
        "barrel": {"cubic metre": 0.158, "litre": 158, "gallon": 42},
        "gallon": {"cubic metre": 0.0037, "litre": 3.785, "barrel": 0.0238},
    }

    select_metric = input('Enter the metric of the input: options are "cubic metre", "litre", "gallon", "barrel"')
    output_metric = input('Enter the metric of the wanted output: options are "cubic metre", "litre", "gallon", "barrel"')

    value = int(input('Enter the value of the input: '))

    if select_metric in metric_factors and output_metric in metric_factors[select_metric]:
        return value * metric_factors[select_metric][output_metric]
    else:
        print("Wrong format")

result = volume_metrics2()
print(f"Result: {result}")


# In[7]:


volume_metrics2()

