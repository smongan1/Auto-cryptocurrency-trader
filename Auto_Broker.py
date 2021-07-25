# -*- coding: utf-8 -*-
"""

"""
#--------INIT--------
import keyboard
import pyautogui
import time
import pyperclip
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statistics

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

def plot_lines(pnts_in,sl,b,std,offset,lin_opt):
        minute_line_points=[(x+offset)*sl+b for x in times_last_minute];
        minute_line_points_p=[x+std for x in minute_line_points];
        minute_line_points_m=[x-std for x in minute_line_points];
        
        plt.plot(times_last_minute,minute_line_points,lin_opt);
        plt.plot(times_last_minute,minute_line_points_p,lin_opt);
        plt.plot(times_last_minute,minute_line_points_m,lin_opt);
        
def buy_fake_crypto(mon,price):
    bought=np.floor(mon/price);
    mon=np.floor((mon-bought*price)*100)/100;
    return bought, mon;

def sell_fake_crypto(c,price):
    money=np.floor(c*price*100)/100;
    return 0, money;
    
is_bought=0;
bought_price=0;
flag=1;
count=0;
start_time=time.time();
plot_time=[];
prices=[];
test_hour=1;
tot=[];
mon=[];
owned_crypto=0;
minute=71;
crypt=[];
std_h=10000000;
hour_out_price_h=0;
plot_hour_price=[];

#--------END INIT--------

#---The Following code is for testing only---
start_money=25;
current_money=start_money;
fake_prices=[]
fake_times=[]
cnt=0;
fake_prices_txt2=[''];
fake_times_txt2=[''];
f = open("C:\\Users\Sean\Python Read_Writes Files\prices.txt","r");
fake_prices_txt=f.read();
f.close();
for x in fake_prices_txt:
    if x=='\n':
        cnt=cnt+1;
        fake_prices_txt2.append('');
    else:
        fake_prices_txt2[cnt]=fake_prices_txt2[cnt]+x
for x in fake_prices_txt2:
    try:
        fake_prices.append(float(x))
    except:
        aa=[];
cnt=0;
f = open("C:\\Users\Sean\Python Read_Writes Files\plot_time.txt","r");
fake_times_txt=f.read();
for x in fake_times_txt:
    if x=='\n':
        cnt=cnt+1;
        fake_times_txt2.append('');
    else:
        fake_times_txt2[cnt]=fake_times_txt2[cnt]+x
for x in fake_times_txt2:
    try:
        fake_times.append(float(x))
    except:
        aa=[];
f.close()
del fake_prices_txt2;
del fake_prices_txt;
del fake_times_txt2;
del fake_times_txt;
del f;
del aa;
del cnt;
#-------------End Test Code-----------------


while(flag):
    
    #a=get_price();
    a=fake_prices[count];
    prices.append(float(a));
    current_price=prices[-1]
    
    #current_time=(time.time()-start_time);
    current_time=fake_times[count];
    plot_time.append(current_time);
    tot.append(current_money+owned_crypto*current_price)#total money is stored per unit time
    crypt.append(owned_crypto*current_price)
    mon.append(current_money)
    
    if count>minute*5+10:
        
        #gets the prices and times in roughly the last minute
        times_last_minute=plot_time[-minute:];
        prices_last_minute=prices[-minute:];
        
        #gets the prices and times in roughly the last 5 minutes
        times_last_V_minute=plot_time[-minute*5:];
        prices_last_V_minute=prices[-minute*5:];
        
        #gets the line of best fit for 5 minutes and 1 minute
        m_1, b_1, r, p, s= stats.linregress(times_last_minute,prices_last_minute)
        m_5, b_5, r, p, s = stats.linregress(times_last_V_minute,prices_last_V_minute)
        
        #fits a polynomial to the data in the last 2 minutes to find local minimum and mximum
        p_5=np.polyfit(times_last_V_minute,prices_last_V_minute,2)
        
        #vertex time location of local min(max)
        vertex_5=-p_5[1]/(2*p_5[0]);
        
        #compares current time to calculated vertex location to determine if they are close
        vertex_test=(abs(vertex_5-current_time)<10);
        
        std_1=np.std(prices_last_minute)
        std_5=np.std(prices_last_V_minute)
        
        plt.cla()
        
        #plt.scatter(times_last_minute,prices_last_minute,c="b")
        #plt.scatter(times_last_V_minute,prices_last_V_minute,c="g")
        
        #plot_lines(times_last_minute,m_1,b_1,std_1,60,"b-")
        #plot_lines(times_last_V_minute,m_5,b_5,std_5,60,"g-")
        
        #Gets the buy price one minute out using fitted lines offset by price std
        minute_out_price=(current_time+minute)*m_1+b_1-std_1/2;
        minute_out_price_V=(current_time+minute)*m_5+b_5-std_5/4;
        
        if count>(minute*60+10):
            times_last_hour=plot_time[-(minute*60+10):]
            prices_last_hour=prices[-(minute*60+10):]
            m_h, b_h, r, p, s = stats.linregress(times_last_hour,prices_last_hour)
            minute_out_price_h=(current_time+minute)*m_h+b_h
            hour_out_price_h=(current_time+minute)*m_h+b_h
            plot_hour_price.append(hour_out_price_h)
            std_h=np.std(prices_last_hour)
            p_h=np.polyfit(times_last_hour,prices_last_hour,2)
        
        #--------------BEGIN LOGIC TESTS TO DETERMINE IF BUY-----------------
        test_minute=current_price<minute_out_price-std_1*5;
        test_good_price=current_price<minute_out_price-(7/2)*std_1;
        
        test_V_minute=current_price<minute_out_price_V;
        test_V_good_price=current_price<minute_out_price_V-(5/4)*std_5;
        
        test_hour=current_price<(hour_out_price_h-std_h/6) or (hour_out_price_h==0);
        test_hour_good_price=(current_price<(hour_out_price_h-std_h/2)) and (hour_out_price_h>0);
        
        good_price_test=test_V_good_price or test_good_price
        
        std_tests=(test_minute and p_5[0]<0)  or (test_V_minute and test_hour)
        
        test_vertex=(vertex_test and p_5[0]<0);
        
        buy_or_tests=std_tests or good_price_test or test_vertex
        enough_money=current_money>current_price
        #--------------END LOGIC TESTS TO DETERMINE IF BUY-----------------
        
        #Gets the sell price one minute out using fitted lines offset by price std
        minute_out_price=(plot_time[-1]+minute)*m_1+b_1+std_1/2;
        minute_out_price_V=(plot_time[-1]+minute)*m_5+b_5+std_5/4;
        
        #--------------BEGIN LOGIC TESTS TO DETERMINE IF SELL-----------------
        test_minute=current_price>minute_out_price;
        test_good_price=current_price>minute_out_price+(1/2)*std_5+3*std_5;
        
        test_hour=current_price<(hour_out_price_h+std_h/6) or (hour_out_price_h==0);
        test_hour_good_price=(current_price<(hour_out_price_h+std_h/2)) and (hour_out_price_h>0);
        
        test_V_minute=current_price>minute_out_price_V;
        test_V_good_price=current_price>minute_out_price_V+(3/4)*std_5;
        
        std_tests=(test_minute and current_price>bought_price) or (test_V_minute and test_hour)
        
        good_price_test=test_V_good_price or test_good_price
        
        test_vertex=(vertex_test and p_5[0]>0);
        sell_or_tests=std_tests or good_price_test or test_vertex
        #--------------END LOGIC TESTS TO DETERMINE IF SELL-----------------
        
        
        if buy_or_tests and enough_money and (not is_bought):
            #current_money=buy_crypto(current_money,prices[-1]);
            buy, current_money=buy_fake_crypto(current_money,current_price)
            owned_crypto=owned_crypto+buy;
            bought_price=current_price;
            is_bought=1;
        else:
            if (sell_or_tests or current_price>1.003*bought_price)and is_bought:
                #current_money=current_money+sell_crypto(owned_crypto,prices[-1]);
                owned_crypto, sell_money=sell_fake_crypto(owned_crypto,current_price)
                current_money=sell_money+current_money;
                is_bought=0;
            
        if mon[-1]<mon[-300]:
            plot_op='-r';
        else:
            plot_op='-g';
        
        plt.plot(plot_time[-300:],tot[-300:], plot_op)
        #plt.plot(plot_time[-300:],mon[-300:], '-b')
        #plt.plot(plot_time[-300:],crypt[-300:], '-y')
        #plt.ylim(24.95,25.35)
        plt.show()
        plt.pause(0.0001)
        
    count=count+1;
    if count>20000:
        flag=0;
        
    #time.sleep(1-time.time()+current_time+start_time)
    
    
    
        
    

