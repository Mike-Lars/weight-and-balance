
airplanes = {'n512nd':{'empty_weight': 1725.4, 
                       'empty_arm': 41.345, 
                       'empty_moment': 71336.8, 
                       'front_pax_arm': 37.0,
                       'rear_pax_arm': 73.0,
                       'fuel_arm': 48.0,
                       'baggage_arm': 95.0
                      },
             'n566nd':{'empty_weight': 1725.875, 
                       'empty_arm': 41.314, 
                       'empty_moment': 71302.56, 
                       'front_pax_arm': 37.0,
                       'rear_pax_arm': 73.0,
                       'fuel_arm': 48.0,
                       'baggage_arm': 95.0
                      },
             'n551nd':{'empty_weight': 1724.2, 
                       'empty_arm': 41.27, 
                       'empty_moment': 71170.97, 
                       'front_pax_arm': 37.0,
                       'rear_pax_arm': 73.0,
                       'fuel_arm': 48.0,
                       'baggage_arm': 95.0
                      },
             'n5138q':{'empty_weight': 1714.1, 
                       'empty_arm': 41.81, 
                       'empty_moment': 71668.0, 
                       'front_pax_arm': 37.0,
                       'rear_pax_arm': 73.0,
                       'fuel_arm': 48.0,
                       'baggage_arm': 95.0
                      },
             'n6318d':{'empty_weight': 1675.3, 
                       'empty_arm': 40.35, 
                       'empty_moment': 67600.35, 
                       'front_pax_arm': 37.0,
                       'rear_pax_arm': 73.0,
                       'fuel_arm': 48.0,
                       'baggage_arm': 95.0
                      },
             'n6318l':{'empty_weight': 1703.1, 
                       'empty_arm': 41.6, 
                       'empty_moment': 70848.96, 
                       'front_pax_arm': 37.0,
                       'rear_pax_arm': 73.0,
                       'fuel_arm': 48.0,
                       'baggage_arm': 95.0
                      },
             'n6319g':{'empty_weight': 1719.2, 
                       'empty_arm': 41.38, 
                       'empty_moment': 71145.0, 
                       'front_pax_arm': 37.0,
                       'rear_pax_arm': 73.0,
                       'fuel_arm': 48.0,
                       'baggage_arm': 95.0
                      },
            }


print("WB Bot at your service. Type 'done' at any time to finish.\n")
for i in airplanes:
        print('>', i.upper())
        
        
while True:
    airplane = input('\nPlease select your airplane: \n')
    if airplane.lower() in airplanes:
        
        #
        while True:
            frontPax = input('\nFront passenger weight: ')
            if frontPax == 'done':
                print('\nSee you next time!')
                break
            else:
                try:
                    frontPax = int(frontPax)
                    
                    ##
                    while True:
                        rearPax = input('Rear passenger weight: ')
                        if rearPax == 'done':
                            print('\nSee you next time!')
                            break
                        else:
                            try:
                                rearPax = int(rearPax)
                                
                                ###
                                while True:
                                    fuelGal = input('Fuel (in gallons): ')
                                    if fuelGal == 'done':
                                        print('\nSee you next time!')
                                        break
                                    else:
                                        try: 
                                            fuelGal = int(fuelGal)
                                            
                                            ####
                                            while True:
                                                baggage = input('Baggage weight: ')
                                                if baggage == 'done':
                                                    print('\nSee you next time!')
                                                    break
                                                else:
                                                    try:
                                                        baggage = int(baggage)
                                                        
                                                        ## ##
                                                        takeoff_weight = round(airplanes[airplane.lower()]['empty_weight'] + frontPax + rearPax + (fuelGal * 6) + baggage, 2)
                                                        takeoff_moment = round(airplanes[airplane.lower()]['empty_moment'] + (frontPax * airplanes[airplane.lower()]['front_pax_arm']) + (rearPax * airplanes[airplane.lower()]['rear_pax_arm']) + ((fuelGal * 6) * airplanes[airplane.lower()]['fuel_arm']) + (baggage * airplanes[airplane.lower()]['baggage_arm']), 2)
                                                        takeoff_cg = round(takeoff_moment / takeoff_weight, 2)
                                                        print('\n\nHere are your Weight and Balance calculations:\n')
                                                        print('Takeoff weight:', f"{takeoff_weight:,}")
                                                        print('Takeoff CG:', f"{takeoff_cg:,}")
                                                        print('Takeoff moment:', f"{takeoff_moment:,}")
                                                        break
                                                        ## ##
                                                        
                                                    except:
                                                        print('\nEnter baggage weight.')
                                            ####            
                                            break
                                                
                                        except:
                                            print('\nEnter fuel in gallons.')
                                ###            
                                break

                            except:
                                print('\nEnter a number for rear passenger weight.')
                    ##                       
                    break
                     
                except:
                    print('\nEnter a number for front passenger weight.')
        #    
        break
        
        
    elif airplane == 'done':
        print('\nSee you next time!')
        break
    else:
        print("\nPlease enter an airplane tail number, or type 'done': ")
    