from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
# read the csv file
materials = pd.read_csv(Path(__file__).resolve().parent / "semi.csv")
def main():
    def show_materials():
        """Clean missing values in the materials data and display the result."""

        def correct_missing_values():
            numeric_columns = materials.select_dtypes(include="number").columns.drop(
                "Band_Gap", errors="ignore"
            )
            materials[numeric_columns] = materials[numeric_columns].fillna(
                materials[numeric_columns].mean()
            )

            missing_band_gaps = materials["Band_Gap"].isna().sum()
            if missing_band_gaps:
                print(
                    f"Leaving {missing_band_gaps} missing Band_Gap value(s) as unknown."
                )

            remaining_missing = materials.isna().sum().sum()
            if remaining_missing:
                print(f"Warning: {remaining_missing} missing value(s) remain.")
            else:
                print("All missing values have been handled!")
            print('-------------------')
            print(materials)
        correct_missing_values()
    show_materials()
    ############################################################  
    
    def Analyse_the_Data():
        def nums_of_materials():
            print('there is ' + str(len(materials)) + ' materials')
        def average_band_gap():
            average_gap = (materials['Band_Gap'].mean())
            print("The average band gap is " + str(round(average_gap,2)))
        def highest_lowest_band_gap():
            max_gap = materials['Band_Gap'].max()
            min_gap = materials['Band_Gap'].min()
            print('the highest band gap is ' + str(max_gap))
            print('the lowest band gap is ' + str(min_gap))
        def standard_deviation():
            std = materials['Band_Gap'].std(ddof=0)
            print('the standard deviation is '+ str(round(std, 2)))
        nums_of_materials()
        average_band_gap()
        highest_lowest_band_gap()
        standard_deviation()
    print('-----------------------------')
    Analyse_the_Data()
    ############################################################
    
    def deferential_the_materials():
        def materials_band_gap_above_2v():
            band_gap_above_2v = materials['Band_Gap'] >= 2.00
            a_band_gap_above_2v =materials[band_gap_above_2v]
            name_of_material_band_gap_above_2v =a_band_gap_above_2v['material']
            print('the material that its band gap is above 2v: ')
            for i in name_of_material_band_gap_above_2v:
                print(i)
        def element_types():
            type_is_element =materials['Type'] == 'Element'
            element =materials[type_is_element]
            name_of_element = element['material']
            print('the materials that is element: ')
            for i in name_of_element:
                print(i)
                
        def compound_type():
            type_of_compound = materials['Type'] == 'Compound'
            compound = materials[type_of_compound]
            name_of_compound = compound['material']
            print(' the materials that is compound: ')
            for i in name_of_compound:
                print(i)
        materials_band_gap_above_2v()
        print('--------------------')
        element_types()
        print('--------------------')
        compound_type()   
    
    deferential_the_materials()
    ############################################################

    def draw_graph():
        materials_name =np.array(materials['material'],ndmin= 1)
        materials_band_gap =np.array(materials['Band_Gap'],ndmin =1)
        x_axis = materials_name
        y_axis = materials_band_gap
        mp.figure(figsize =(12,6))
        mp.bar(x_axis,y_axis)
        mp.xticks(rotation = 80)
        mp.title('Band Gap of different meterials')
        
        mp.show()
    draw_graph()

main()
      
