# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:19:21 2021

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
if True:  #Used to hide init
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

def poly_test(t_in,p_in,t_offset,sig):
    t_price=sum(p_in[-10:])/10
    t_time=t_in[-1]
    f_times=[2*t_time-x for x in np.flip(t_in)];
    f_prices=np.flip(p_in)
    t_in.extend(f_times)
    p_in.extend(f_prices)
    p_out=np.polyfit(t_in,p_in,2,full=True)
    p=p_out[0]
    r_poly=p_out[1]
    x_pos=-p[1]/(2*p[0]);
    vertex=pow(x_pos,2)*p[0]+x_pos*p[1]+p[2];
    dis_poly=abs(t_price-vertex)
    v_test=dis_poly<t_offset
    p_test=v_test*((sig*p[0])>0)
    if p_test:
        pt_opt='-g'
    else:
        pt_opt='-r'
    plt.plot(t_in,[pow(x,2)*p[0]+x*p[1]+p[2] for x in t_in],pt_opt)
    plt.plot(t_in,p_in,'.b')
    return p_test, r_poly, dis_poly

if True: #Used to hide init
    plot_time=[];prices=[];tot=[];mon=[];crypt=[];plot_hour_price=[];tot_end=[];dd=[];
    is_bought=0;
    bought_price=-1;
    flag=1;
    test_hour=1;
    start_time=time.time();
    owned_crypto=0;
    minute=71;
    hour_out_price_h=0;
    ff=prices.append;
    tt=tot.append;
    pp=plot_time.append;
    count=minute*60+10;
    p_main=0;
    std_m=1;std_v=2/2;std_h=2/2;

#--------END INIT--------

#---The Following code is for testing only---

if True: #Used to hide test code
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
    pr_mean=sum(prices[-1000:])/1000
    if (not is_bought)*(prices[-1]<pr_mean):
        plt.cla()
        #--------------BEGIN LOGIC TESTS TO DETERMINE IF BUY-----------------
    
        tminprice, tgprice=line_test(plot_time[-minute:],prices[-minute:],-std_m,-4*std_m,minute)
        tVminprice, tVgprice=line_test(plot_time[-5*minute:],prices[-5*minute:],-std_v,-4*std_v,minute)
        
        if count>(minute*60+10):
            thprice, thgprice=line_test(plot_time[-60*minute:],prices[-60*minute:],0,-4*std_h,minute)
        else:
            thprice=1; thgprice=1;
            r_min=10^99;
            
        for x in range(300,1260,60):
            pt_in=[plot_time[ii] for ii in range(-x-1,-1,10)]
            pr_in=[prices[ii] for ii in range(-x-1,-1,10)]
            #pt_in=plot_time[-x:]
            #pr_in=prices[-x:]
            p_test, r, dis=poly_test(pt_in,pr_in,1*pow(10,-5),1)
            r=r/x;
            dd.append(dis)
            if r<r_min:
                r_min=r
                p_main=p_test
                x_main=x;
        if p_main:
            plt.show()
            plt.pause(1)
        
        p_test=p_main;
        s_test=(tminprice*tVminprice*thprice);
        buy_or_tests=s_test*p_test
        enough_money=current_money>current_price
        buy_tests=buy_or_tests*enough_money
        
        #--------------END LOGIC TESTS TO DETERMINE IF BUY-----------------
        if buy_tests:
            #current_money=buy_crypto(current_money,prices[-1]);
            buy, current_money=buy_fake_crypto(current_money,current_price)
            owned_crypto=owned_crypto+buy;
            bought_price=current_price;
            is_bought=1;
            #print('buying')
                
    if is_bought*(pr_mean<prices[-1]):
        
        #--------------BEGIN LOGIC TESTS TO DETERMINE IF SELL-----------------
        
        tminprice, tgprice=line_test(plot_time[-minute:],prices[-minute:],std_m,8*std_m,minute)
        tVminprice, tVgprice=line_test(plot_time[-5*minute:],prices[-5*minute:],std_v,8*std_v,minute)
        if count>(minute*60+10):
            thprice, thgprice=line_test(plot_time[-60*minute:],prices[-60*minute:],0,8*std_h,minute)
        else:
            thprice=1; thgprice=1;
        p_test=poly_test(plot_time[-5*minute:],prices[-5*minute:],5000,1)
        gpt=tVgprice or tgprice;
        s_test=(tminprice*tVminprice*thprice);
        sell_or_tests=s_test or gpt or p_test
        enough_money=current_money>current_price
        p_ratio=current_price/bought_price;
        sell_tests=(sell_or_tests or p_ratio>1.003)
        sell_tests=True;
        
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
          
    if np.mod(count,1000)==1:
       print(count)
        #plt.cla()
        #plt.plot(plot_time[-300:],tot[-300:], plot_op)
        #plt.show()
        #plt.pause(0.0001)
        
        
        
    count=count+1;
    if count>20000:
        flag=0;

    
        
    #time.sleep(1-time.time()+current_time+start_time)
    
    tot_end.append(tot[-1])
    
        
    

