# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:18:16 2021

@author: Sean
"""

# -*- coding: utf-8 -*-
"""

"""
#--------INIT--------
if True: #Hides import parameters
    import keyboard
    import pyautogui
    import time
    import pyperclip
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import stats
    import statistics
    fl=np.floor

def get_price():
    #clicks on current price 3 times to highlight full price
    pyautogui.click(x=2325, y=231); 
    time.sleep(.001);
    pyautogui.click(x=2325, y=231);
    time.sleep(.001);
    pyautogui.click(x=2325, y=231);
    #copies price
    pyautogui.hotkey('ctrl', 'c');
    #pastes price into "value"
    value=pyperclip.paste();
    #clicks on blank part of webpage to refresh clicks
    pyautogui.click(x=2425, y=231);
    #checks to see if "value" is a number
    try:
        value2=float(value[1:])
    except:
        print("Invalid number found. Please ensure the robinhood tab is selected.")
        return
    return value2

def plot_lines(pnts,sl,b,std,offset,lin_opt):
    minute_line_points=[(x+offset)*sl+b for x in pnts];
    minute_line_points_p=[x+std for x in minute_line_points];
    minute_line_points_m=[x-std for x in minute_line_points];
    plt.plot(pnts,minute_line_points,lin_opt);
    plt.plot(pnts,minute_line_points_p,lin_opt);
    plt.plot(pnts,minute_line_points_m,lin_opt);
        
def buy_fake_crypto(mon,price):
    bought=fl(mon/price);
    mon=fl((mon-bought*price)*100)/100;
    return bought, mon;

def sell_fake_crypto(c,price):
    money=fl(c*price*100)/100;
    return 0, money;

def line_test(times,prices,s_1,s_2,t_offset):
    m, b, r, p, s=stats.linregress(times,prices)
    s=np.std(prices)
    out_price=(times[-1]+t_offset)*m+b;
    target=(out_price+s_1*s);
    test=(s_1*(current_price-target))>0;
    target=(out_price+s_2*s);
    test_good_price=(s_2*(current_price-target))>0;
    return test, test_good_price

def poly_test(times,prices,t_offset,sig):
    p=np.polyfit(times,prices,2)
    vertex=-p[1]/(2*p[0]);
    v_test=abs(times[-1]-vertex)<t_offset
    p_test=v_test*sig*p[0]>0
    return p_test

if True:  #Hides init parameters  
    is_bought=0;
    bought_price=-1;
    flag=1;
    start_time=time.time();
    plot_time=[];
    prices=[];
    test_hour=1;
    tot=[];
    mon=[];
    owned_crypto=0;
    minute=71;
    crypt=[];
    hour_out_price_h=0;
    plot_hour_price=[];
    ff=prices.append;
    tt=tot.append;
    pp=plot_time.append;
    count=60*minute+10;
    std_m=2;std_v=1;std_h=1/2;
#--------END INIT--------

#---The Following code is for testing only---
if True: #Hides test parameters
    start_money=25; current_money=start_money; fake_prices=[]; fake_times=[]; cnt=0; fake_prices_txt2=['']; fake_times_txt2=['']; f = open("C:\\Users\Sean\Python Read_Writes Files\prices.txt","r"); fake_prices_txt=f.read(); f.close();
    for x in fake_prices_txt:
        if x=='\n':
            cnt=cnt+1; fake_prices_txt2.append('');
        else:
            fake_prices_txt2[cnt]=fake_prices_txt2[cnt]+x
    for x in fake_prices_txt2:
        try:
            fake_prices.append(float(x))
        except:
            aa=[];
    cnt=0;
    f = open("C:\\Users\Sean\Python Read_Writes Files\plot_time.txt","r"); fake_times_txt=f.read();
    for x in fake_times_txt:
        if x=='\n':
            cnt=cnt+1; fake_times_txt2.append('');
        else:
            fake_times_txt2[cnt]=fake_times_txt2[cnt]+x
    for x in fake_times_txt2:
        try:
            fake_times.append(float(x))
        except:
            aa=[];
    f.close()
    del fake_prices_txt2; del fake_prices_txt; del fake_times_txt2; del fake_times_txt; del f; del aa; del cnt;
#-------------End Test Code-----------------


for cnt in range(0,count-1):
    #a=get_price();
    a=fake_prices[cnt];
    ff(float(a));
    current_price=prices[-1]
        
    #current_time=(time.time()-start_time);
    current_time=fake_times[cnt];
    pp(current_time);
    tt(current_money+owned_crypto*current_price)#total money is stored per unit time
    #crypt.append(owned_crypto*current_price)
    #mon.append(current_money)
    


while(flag):
    a=fake_prices[count];
    ff(float(a));
    current_price=prices[-1]
    
    #current_time=(time.time()-start_time);
    current_time=fake_times[count];
    pp(current_time);
    tt(current_money+owned_crypto*current_price)#total money is stored per unit time
    #crypt.append(owned_crypto*current_price)
    #mon.append(current_money)
    
    if (not is_bought):
        
        #--------------BEGIN LOGIC TESTS TO DETERMINE IF BUY-----------------
    
        tminprice, tgprice=line_test(plot_time[-minute:],prices[-minute:],-std_m,-2*std_m,minute)
        tVminprice, tVgprice=line_test(plot_time[-5*minute:],prices[-5*minute:],-std_v,-2*std_v,minute)
        thprice, thgprice=line_test(plot_time[-60*minute:],prices[-60*minute:],0,-2*std_h,minute)
        thprice=1; thgprice=1;
        p_test=poly_test(plot_time[-5*minute:],prices[-5*minute:],50,-1)
        gpt=tVgprice or tgprice;
        s_test=(tminprice and tVminprice and thprice);
        buy_or_tests=s_test or gpt or p_test
        enough_money=current_money>current_price
        buy_tests=buy_or_tests and enough_money
        
        #--------------END LOGIC TESTS TO DETERMINE IF BUY-----------------
        if buy_tests:
            #current_money=buy_crypto(current_money,prices[-1]);
            buy, current_money=buy_fake_crypto(current_money,current_price)
            owned_crypto=owned_crypto+buy;
            bought_price=current_price;
            is_bought=1;
            #print('buying')
                
                
    if is_bought:
        
        #--------------BEGIN LOGIC TESTS TO DETERMINE IF SELL-----------------
        
        tminprice, tgprice=line_test(plot_time[-minute:],prices[-minute:],std_m,2*std_m,minute)
        tVminprice, tVgprice=line_test(plot_time[-5*minute:],prices[-5*minute:],std_v,2*std_v,minute)
        thprice, thgprice=line_test(plot_time[-60*minute:],prices[-60*minute:],0,2*std_h,minute)
        thprice=1; thgprice=1;
        p_test=poly_test(plot_time[-5*minute:],prices[-5*minute:],50,1)
        gpt=tVgprice or tgprice;
        s_test=(tminprice and tVminprice and thprice);
        sell_or_tests=s_test or gpt or p_test
        enough_money=current_money>current_price
        p_ratio=current_price/bought_price;
        sell_tests=sell_or_tests or (p_ratio>1.003)
        
        #--------------END LOGIC TESTS TO DETERMINE IF SELL-----------------

        if sell_tests:
            #current_money=current_money+sell_crypto(owned_crypto,prices[-1]);
            owned_crypto, sell_money=sell_fake_crypto(owned_crypto,current_price)
            current_money=sell_money+current_money;
            is_bought=0;
            #print('selling')
            
        #if tot[-1]<tot[-300]:
        #   plot_op='-r';
        #else:
        #    plot_op='-g';
        
        #if np.mod(count,1000)==1:
        #   print(count)
            #plt.cla()
            #plt.plot(plot_time[-300:],tot[-300:], plot_op)
            #plt.show()
            #plt.pause(0.0001)
        
        
        
    count=count+1;
    if count>20000:
        flag=0;
    
    
        
    #time.sleep(1-time.time()+current_time+start_time)
    
    
    
        
    

