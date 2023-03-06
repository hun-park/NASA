This dataset is part of a series of datasets, where batteries are continuously cycled with randomly generated current profiles.   
Reference charging and discharging cycles are also performed after a fixed interval of randomized usage to provide reference benchmarks for battery state of health.   


~~1. Battery_Uniform_Distribution_Charge_Discharge_DataSet_2Post.zip   
*(Identified as RW9, RW10, RW11 and RW12)*  
	* In this dataset, four 18650 Li-ion batteries were continuously operated using a sequence of charging and discharging currents between -4.5A and 4.5A.   
	* This type of charging and discharging operation is referred to here as random walk (RW) operation.   
	* Each of the loading periods lasted 5 minutes, and after 1500 periods (about 5 days) a series of reference charging and discharging cycles were performed in order to provide reference benchmarks for battery state health.~~   

2. Battery_Uniform_Distribution_Discharge_Room_Temp_DataSet_2Post.zip   
*(Identified as RW3, RW4, RW5 and RW6)*   
	* In this dataset, four 18650 Li-ion batteries were continuously operated by repeatedly charging them to 4.2V and then discharging them to 3.2V using a randomized sequence of discharging currents between 0.5A and 4A.   
	* This type of discharging profile is referred to here as random walk (RW) discharging.   
	* After every fifty RW cycles a series of reference charging and discharging cycles were performed in order to provide reference benchmarks for battery state health.   

~~3. Battery_Uniform_Distribution_Variable_Charge_Room_Temp_DataSet_2Post.zip   
*(Identified as RW1, RW2, RW7 and RW8)*   
	* In this dataset, four 18650 Li-ion batteries were continuously operated by repeatedly discharging them to 3.2V using a randomized sequence of discharging currents between 0.5A and 4A. 
	* This type of discharging profile is referred to here as random walk (RW) discharging.   
	* After each discharging cycle the batteries were charged for a randomly selected duration between 0.5 hours and 3 hours.   
	* After every fifty RW cycles a series of reference charging and discharging cycles were performed in order to provide reference benchmarks for battery state health.~~   

4. RW_Skewed_High_40C_DataSet_2Post.zip   
*(Identified as RW25, RW26, RW27 and RW28)*   
	* In this dataset, four 18650 Li-ion batteries were continuously operated by repeatedly charging them to 4.2V and then discharging them to 3.2V using a randomized sequence of discharging currents between 0.5A and 5A.   
	* This type of discharging profile is referred to here as random walk (RW) discharging.   
	* A customized probability distribution is used in this experiment to select a new load setpoint every 1 minute during RW discharging operation.   
	* The custom probability distribution was designed to be skewed towards selecting higher currents.   
	* The ambient temperature at which the batteries are cycled was held at approximately 40C for these experiments.   

5. RW_Skewed_High_Room_Temp_DataSet_2Post.zip   
*(Identified as RW17, RW18, RW19 and RW20)*   
	* In this dataset, four 18650 Li-ion batteries were continuously operated by repeatedly charging them to 4.2V and then discharging them to 3.2V using a randomized sequence of discharging currents between 0.5A and 5A.   
	* This type of discharging profile is referred to here as random walk (RW) discharging.   
	* A customized probability distribution is used in this experiment to select a new load setpoint every 1 minute during RW discharging operation.   
	* The custom probability distribution was designed to be skewed towards selecting higher currents.   

6. RW_Skewed_Low_40C_DataSet_2Post.zip   
*(Identified as RW21, RW22, RW23 and RW24)*    
	* In this dataset, four 18650 Li-ion batteries were continuously operated by repeatedly charging them to 4.2V and then discharging them to 3.2V using a randomized sequence of discharging currents between 0.5A and 5A.   
	* This type of discharging profile is referred to here as random walk (RW) discharging.   
	* A customized probability distribution is used in this experiment to select a new load setpoint every 1 minute during RW discharging operation.   
	* The custom probability distribution was designed to be skewed towards selecting lower currents.   
	* The ambient temperature at which the batteries are cycled was held at approximately 40C for these experiments.   

7. RW_Skewed_Low_Room_Temp_DataSet_2Post.zip   
*(Identified as RW13, RW14, RW15 and RW16)*   
	* In this dataset, four 18650 Li-ion batteries were continuously operated by repeatedly charging them to 4.2V and then discharging them to 3.2V using a randomized sequence of discharging currents between 0.5A and 5A.   
	* This type of discharging profile is referred to here as random walk (RW) discharging.   
	* A customized probability distribution is used in this experiment to select a new load setpoint every 1 minute during RW discharging operation.   
	* The custom probability distribution was designed to be skewed towards selecting lower currents.   


# Structure ***type*** #
* data ***dict***
	+ step ***dict*** **(ex RW26)**
		+ comment ***list*** **(#s 16,666)**
			+ comment ***str***
		+ type ***list*** **(#s 16,666)**
			+ type ***str***
		+ time ***list*** **(#s 16,666)**
			+ per 1 set ***list***
		+ relativeTime ***list*** **(#s 16,666)** **(starts with 0)**
			+ per 1 set ***list*** **(not monotonic)**
		+ voltage ***list*** **(#s 16,666)**
			+ per 1 set ***list***
		+ current ***list*** **(#s 16,666)**
			+ per 1 set ***list***
		+ temperature ***list*** **(#s 16,666)**
			+ per 1 set ***list***
		+ date ***list*** **(#s 16,666)**
			+ date ***str***
	+ procedure ***str***
	+ description ***str***
