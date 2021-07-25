# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:00:55 2021

@author: Sean
"""

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

std=[1.7,1.8]
std=[1.7,1.8]
std=1.7
tot_fin=[];
plotters=[];

if True:  #Hides init parameters
    plot_time=[];crypt=[];plot_hour_price=[];mon=[];tot=[];prices=[];
    is_bought=0;
    bought_price=-1;
    flag=1;
    start_time=time.time();
    test_hour=1;
    owned_crypto=0;
    minute=59;
    hour_out_price_h=0;
    ff=prices.append;
    tt=tot.append;
    pp=plot_time.append;
    count=60*minute+10;
    std_m=std;std_v=std/2;std_h=std/4;
    set_limit=0;
    limit_price=0;
    buy_time=0;
#--------END INIT--------

#---The Following code is for testing only---
if True: #Hides test parameters
    start_money=25; current_money=start_money; fake_prices=[]; fake_times=[]; cnt=0; fake_prices_txt2=['']; fake_times_txt2=['']; 
    f = open("C:\\Users\Sean\Python Read_Writes Files\prices2.txt","r"); fake_prices_txt=f.read(); f.close();
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
    f = open("C:\\Users\Sean\Python Read_Writes Files\\times2.txt","r"); fake_times_txt=f.read();f.close()
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
    

sell_cnt=0;
buy_cnt=0;
while(flag):
    if set_limit==1:
        set_limit=0
        for i in range(0,5):
            a=fake_prices[count];
            count=count+1
            ff(float(a));
            current_price=prices[-1]
            current_time=fake_times[count];
            pp(current_time);
            tt(current_money+owned_crypto*current_price)
            
    if is_bought:
        plt_v='g'
        if limit_price>0 and limit_price<current_price:
            owned_crypto, sell_money=sell_fake_crypto(owned_crypto,current_price)
            current_money=sell_money+current_money;
            limit_price=0
            is_bought=0;
            sell_cnt=sell_cnt+1
    else:
        plt_v='r'
        if limit_price>current_price:
            buy, current_money=buy_fake_crypto(current_money,current_price)
            owned_crypto=owned_crypto+buy;
            bought_price=current_price;
            buy_cnt=buy_cnt+1
            limit_price=0
            is_bought=1
            
    a=fake_prices[count];
    ff(float(a));
    current_price=prices[-1]
    current_time=fake_times[count];
    pp(current_time);
    tt(current_money+owned_crypto*current_price)#total money is stored per unit time
    
   #if limit_price>0 and is_bought:
        
    
    if (limit_price==0 or (current_time-buy_time)>60):
        if (not is_bought):
            
            #--------------BEGIN LOGIC TESTS TO DETERMINE IF BUY-----------------
            
            std_d=std
            std_m=std_d;std_v=std_d/2;std_h=std_d/4;
            tminprice, tgprice=line_test(plot_time[-5*minute:],prices[-5*minute:],-std_m,-2*std_m,minute)
            tVminprice, tVgprice=line_test(plot_time[-10*minute:],prices[-10*minute:],-std_v,-2*std_v,minute)
            thprice, thgprice=line_test(plot_time[-60*minute:],prices[-60*minute:],0,-2*std_h,minute)
            gpt=tVgprice or tgprice;
            s_test=(tminprice and tVminprice and thprice);
            buy_or_tests=s_test or gpt
            enough_money=current_money>current_price
            buy_tests=buy_or_tests and enough_money
            
            #--------------END LOGIC TESTS TO DETERMINE IF BUY-----------------
            
            if buy_tests:
                if set_limit==0:
                    set_limit=1;
                    limit_price=current_price
                    buy_time=current_time
                
        if is_bought:
            
            #--------------BEGIN LOGIC TESTS TO DETERMINE IF SELL-----------------
            
            std_d=std*(2)
            std_m=std_d;std_v=std_d/2;std_h=std_d/4;
            tminprice, tgprice=line_test(plot_time[-5*minute:],prices[-5*minute:],std_m,2*std_m,minute)
            tVminprice, tVgprice=line_test(plot_time[-10*minute:],prices[-10*minute:],std_v,2*std_v,minute)
            thprice, thgprice=line_test(plot_time[-60*minute:],prices[-60*minute:],0,2*std_h,minute)
            gpt=tVgprice or tgprice
            s_test=(tminprice and tVminprice and thprice);
            sell_or_tests=s_test or gpt
            enough_money=current_money>current_price
            p_ratio=current_price/bought_price;
            sell_tests=sell_or_tests or (p_ratio>1.003)
            
            #--------------END LOGIC TESTS TO DETERMINE IF SELL-----------------
            if sell_tests:
                if set_limit==0:
                    set_limit=1;
                    limit_price=current_price
                    print()
    count=count+1;
    if count>20000:
        flag=0;
    if np.mod(count,10)==0:
        plt.cla()
        plt.plot(plot_time[(count-300):count],tot[(count-300):count])
        plt.plot(plot_time[(count-300):count],[x*460 for x in prices[(count-300):count]])
        if limit_price>0:
            plt.plot(plot_time[(count-300):count],[limit_price*460 for x in plot_time[(count-300):count]],plt_v)
        plt.show()
        plt.pause(0.1)
     
plt.plot(tot)        
tot_fin.append(tot[-1])
plt.show()
plt.pause(0.001)
#time.sleep(1-time.time()+current_time+start_time)
    
    
    
        
    

