# -*- coding: utf-8 -*-
"""
Created on Sat March 6 13:01 2021

@author: Sean
"""


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
    from tkinter import *
    
def cancel_order(ref):
    m_ps=pyautogui.Point(x=ref[0],y=(ref[1]-40))
    h_ps=pyautogui.Point(x=(m_ps[0]+225),y=m_ps[1])
    o_ps=pyautogui.Point(x=h_ps[0],y=(h_ps[1]+360))
    c_ps=pyautogui.Point(x=o_ps[0],y=(o_ps[1]+212))
    pyautogui.click(h_ps);
    time.sleep(0.1)
    pyautogui.click(ref);
    time.sleep(2)
    pyautogui.click(o_ps);
    time.sleep(0.5)
    pyautogui.click(c_ps);
    time.sleep(0.5)
    pyautogui.click(m_ps);
    time.sleep(0.1)
    pyautogui.click(ref);
    time.sleep(2)
    
def get_cash_and_crypto(c_pos):
    pyautogui.click(c_pos[9]);
    time.sleep(0.05)
    cm=get_curr_cash([c_pos[7][0],c_pos[7][1]])
    time.sleep(0.05)
    pyautogui.click(c_pos[10]);
    time.sleep(0.05)
    oc=get_curr_cash([c_pos[7][0]-10,c_pos[7][1]-50])
    time.sleep(0.05)
    pyautogui.click(c_pos[9]);
    time.sleep(0.05)
    return cm, oc

def review_and_submit(rop,sop):
    pyautogui.click(x=rop[0],y=rop[1])
    time.sleep(1);
    pyautogui.click(x=sop[0],y=sop[1]);
    time.sleep(.1);

    
def buy_crypto(c_pos, pr_in):
    time.sleep(0.05)
    cash_ps=[c_pos[7][0],c_pos[7][1]]
    cash=get_curr_cash(cash_ps)
    limit_set(c_pos[1], c_pos[2], c_pos[4], pr_in)
    three_click(c_pos[3]);
    pyautogui.hotkey('backspace');
    time.sleep(0.05);
    type_word(str(cash))
    review_and_submit(c_pos[5], c_pos[6])
    time.sleep(0.05)
    pyautogui.click(c_pos[10]);
    time.sleep(0.05)
    crypt_ps=[c_pos[7][0]-10,c_pos[7][1]-50]
    crypt=get_curr_cash(crypt_ps)
    
    
def sell_crypto(c_pos, pr_in):
    time.sleep(0.05)
    limit_set(c_pos[1], c_pos[2], c_pos[4], pr_in)
    crypt_ps=c_pos[8]
    crypt=get_curr_cash(crypt_ps)
    three_click(c_pos[3]);
    pyautogui.hotkey('backspace');
    time.sleep(0.05);
    type_word(str(crypt))
    rop=[c_pos[5][0],c_pos[5][1]-50];
    sop=[rop[0],rop[1]+225];
    review_and_submit(rop, sop)
    pyautogui.click(c_pos[9]);
    time.sleep(0.05);
    #cash_ps=[c_pos[7][0],c_pos[7][1]]
    #cash=get_curr_cash(cash_ps)

    
def type_word(in_w):
    for x in in_w:
        pyautogui.hotkey(x);
        time.sleep(.08);

def three_click(posi2):
    posi=pyautogui.Point(x=posi2[0],y=posi2[1])
    pyautogui.click(posi);
    time.sleep(0.05);
    pyautogui.click(posi);
    time.sleep(0.05);
    pyautogui.click(posi);
    time.sleep(0.05);
    
def get_curr_cash(b_p_ps):
    three_click(b_p_ps);
    pyautogui.hotkey('ctrl', 'c');
    b_p_txt=pyperclip.paste();
    if b_p_txt[0]=='$':
        for x in range(1,len(b_p_txt)):
            if b_p_txt[x]=='.':
                ppos=x
                time.sleep(.05);
        bp=b_p_txt[1:(ppos+3)]
    else:
        ppos=''
        for x in range(0,len(b_p_txt)):
            if b_p_txt[x]==' ' and ppos=='':
                ppos=x
                time.sleep(.05);
        bp=b_p_txt[0:(ppos)]
    
    if bp[0]=='E':
        bp=0;
    return float(bp)

def limit_set(d_d_pos, l_ps, l_a_ps, pr_in):
    pyautogui.click(d_d_pos); 
    time.sleep(0.2);
    pyautogui.click(l_ps);
    time.sleep(0.1);
    three_click(l_a_ps);
    pyautogui.hotkey('backspace');
    type_word(str(pr_in))
    
def in_doge_chk(c_pos,s_in):
    est_pos=[c_pos[9][0],c_pos[9][1]+155]
    three_click(est_pos)
    pyautogui.hotkey('ctrl', 'c');
    txt=pyperclip.paste();
    if (not txt[-1]==s_in):
        cur_ch_pos=[c_pos[9][0],c_pos[9][1]+57]
        pyautogui.click(x=cur_ch_pos[0],y=cur_ch_pos[1])
        
def get_click_pos():
    input("Place cursor on prices $ sign and press enter...")
    price_ps=pyautogui.position();
    input("Place cursor on limit order drop down and press enter...")
    drop_down_ps=pyautogui.position();
    limit_ps=pyautogui.Point(x=(drop_down_ps[0]-70),y=(drop_down_ps[1]+115));
    dollar_amt_ps=pyautogui.Point(x=drop_down_ps[0]-20,y=(drop_down_ps[1]+60));
    limit_amt_ps=pyautogui.Point(x=dollar_amt_ps[0],y=(dollar_amt_ps[1]+47));
    buy_opt_ps=pyautogui.Point(x=(drop_down_ps[0]-190),y=(drop_down_ps[1]));
    sell_opt_ps=pyautogui.Point(x=(buy_opt_ps[0]+80),y=buy_opt_ps[1]);
    rev_order_ps=pyautogui.Point(x=sell_opt_ps[0],y=(sell_opt_ps[1]+242));
    sub_order_ps=pyautogui.Point(x=sell_opt_ps[0],y=(sell_opt_ps[1]+242+190));
    buy_pow_ps=pyautogui.Point(x=sell_opt_ps[0],y=(sell_opt_ps[1]+315));
    crypto_amt_ps=pyautogui.Point(x=sell_opt_ps[0],y=(sell_opt_ps[1]+265));
    input("Place cursor on Refresh position and press enter...")
    refresh_ps=pyautogui.position();
    #out=[price_ps, drop_down_ps, limit_ps, dollar_amt_ps, limit_amt_ps, rev_order_ps, sub_order_ps, 
    #        buy_pow_ps, crypto_amt_ps, buy_opt_ps, sell_opt_ps, refresh_ps]
        
    return [price_ps, drop_down_ps, limit_ps, dollar_amt_ps, limit_amt_ps, rev_order_ps, sub_order_ps, 
            buy_pow_ps, crypto_amt_ps, buy_opt_ps, sell_opt_ps, refresh_ps]

#price_pos, drop_down_pos, limit_pos, dollar_amt_pos, limit_amt_pos, rev_order_pos, sub_order_pos, buy_pow_pos=get_click_pos()
#set_and_buy( drop_down_pos, limit_pos, dollar_amt_pos, limit_amt_pos, rev_order_pos, sub_order_pos, buy_pow_pos, 0)

def get_price(pnt_in):
    #clicks on current price 3 times to highlight full price
    three_click(pnt_in); 
    #copies price
    pyautogui.hotkey('ctrl', 'c');
    #pastes price into "value"
    value=pyperclip.paste();
    #clicks on blank part of webpage to refresh clicks
    pyautogui.click(x=pnt_in[0]+200, y=pnt_in[1]);
    #checks to see if "value" is a number
    try:
        value2=float(value[1:])
    except:
        print("Invalid number found. Please ensure the robinhood tab is selected.")
        return
    return value2

def line_test(times,prices,s_1,s_2,t_offset):
    c_price=prices[-1]
    s=np.std(prices)
    pri_len=len(prices)
    if pri_len<2000:
        m, b, r, p, s=stats.linregress(times,prices)
        out_price=(times[-1]+t_offset)*m+b;
        target=(out_price+s_1*s);
        test=(s_1*(c_price-target))>0;
        target=(out_price+s_2*s);
        test_good_price=(s_2*(c_price-target))>0;
    else:
        target=sum(prices)/pri_len;
        test=(s_1*(c_price-target))>0;
        test_good_price=(s_2*(c_price-target))>0;
    return test, test_good_price

std=1.7
tot_fin=[];
plotters=[];

if True:  #Hides init parameters
    click_positions=get_click_pos()
    plot_time=[];crypt=[];plot_hour_price=[];mon=[];tot=[];prices=[];
    is_bought=0;
    bought_price=-1;
    flag=1;
    start_time=time.time();
    test_hour=1;
    owned_crypto=0;
    minute=80;
    hour_out_price_h=0;
    tt=tot.append;
    count=120*minute+10;
    set_limit=0;
    limit_price=0;
    buy_time=0;
    cancel=0;
    can_buy=0;
    can_sell=0;
    #start_money=25; current_money=start_money;
#--------END INIT--------

for cnt in range(0,count-1):
    a=get_price(click_positions[0]);
    prices.append(float(a));
    current_price=prices[-1]
    current_time=time.time()-start_time;
    plot_time.append(current_time);
    
current_money, owned_crypto=get_cash_and_crypto(click_positions)
tt(current_money+owned_crypto*current_price)

while(flag):
    if set_limit==1:
        set_limit=0
        for i in range(0,5):
            a=get_price(click_positions[0]);
            count=count+1
            prices.append(float(a));
            current_price=prices[-1]
            current_time=time.time()-start_time;
            plot_time.append(current_time);
        pltest=sum(prices[-4:])/4
        pltest1=min(prices[-4:])
        pltest2=max(prices[-4:])
    if limit_price>0:
        if is_bought:
            plt_v='g'
            if limit_price<pltest:
                pyautogui.click(click_positions[11]);
                time.sleep(3)
                in_doge_chk(click_positions,'t')
                current_money, owned_crypto=get_cash_and_crypto(click_positions)
                tt(current_money+owned_crypto*current_price)
                pyautogui.click(click_positions[10]);
                sell_crypto(click_positions,pltest2)
                pyautogui.click(click_positions[11]);
                time.sleep(2)
                limit_price=0
                is_bought=0;
                cancel=1
        else:
            plt_v='r'
            if limit_price>pltest:
                pyautogui.click(click_positions[11])
                time.sleep(3)
                in_doge_chk(click_positions,'E')
                tt(current_money+owned_crypto*current_price)
                pyautogui.click(click_positions[9]);
                buy_crypto(click_positions,pltest1)
                pyautogui.click(click_positions[11]);
                time.sleep(3)
                current_money, owned_crypto=get_cash_and_crypto(click_positions)
                bought_price=pltest;
                is_bought=1
                limit_price=0
                cancel=1
            
    a=get_price(click_positions[0]);
    prices.append(float(a));
    current_price=prices[-1]
    current_time=time.time()-start_time;
    plot_time.append(current_time);
    prices=prices[-(120*minute+10):]
    plot_time=plot_time[-(120*minute+10):]
    
   #if limit_price>0 and is_bought:
        
    
    if (limit_price==0 or (current_time-buy_time)>120):
        if cancel==1 and (current_time-buy_time)>120:
            cancel_order(click_positions[11])
            pyautogui.click(click_positions[11])
            time.sleep(2)
            cancel=0
            cash=get_curr_cash(click_positions[7])
            set_limit=0;
            limit_price=0;
            if cash<1:
                is_bought=1;
            else:
                is_bought=0;
        if (not is_bought):
            
            #--------------BEGIN LOGIC TESTS TO DETERMINE IF BUY-----------------
            
            std_d=std
            std_m=std_d;std_v=std_d/2;std_h=std_d/4;
            tminprice, tgprice=line_test(plot_time[-5*minute:],prices[-5*minute:],-std_m,-2*std_m,minute)
            tVminprice, tVgprice=line_test(plot_time[-10*minute:],prices[-10*minute:],-std_v,-2*std_v,minute)
            thprice, thgprice=line_test(plot_time[-120*minute:],prices[-120*minute:],-1*std_h,-2*std_h,minute)
            gpt=tVgprice or tgprice;
            s_test=(tminprice and tVminprice and thprice);
            buy_or_tests=s_test or gpt
            #enough_money=current_money>current_price
            buy_tests=buy_or_tests
            
            #--------------END LOGIC TESTS TO DETERMINE IF BUY-----------------
            
            if buy_tests:
                if set_limit==0:
                    set_limit=1;
                    limit_price=current_price
                    buy_time=current_time
                    can_buy=can_buy+1;
                    
                
        else:
            
            #--------------BEGIN LOGIC TESTS TO DETERMINE IF SELL-----------------
            
            std_d=std*(2.2)
            std_m=std_d;std_v=std_d/2;std_h=std_d/4;
            tminprice, tgprice=line_test(plot_time[-5*minute:],prices[-5*minute:],std_m,2*std_m,minute)
            tVminprice, tVgprice=line_test(plot_time[-10*minute:],prices[-10*minute:],std_v,2*std_v,minute)
            thprice, thgprice=line_test(plot_time[-120*minute:],prices[-120*minute:],1*std_h,2*std_h,minute)
            gpt=tVgprice or tgprice
            s_test=(tminprice and tVminprice and thprice);
            sell_or_tests=s_test or gpt
            p_ratio=current_price/bought_price;
            sell_tests=sell_or_tests or (p_ratio>1.003)
            
            #--------------END LOGIC TESTS TO DETERMINE IF SELL-----------------
            if sell_tests:
                if set_limit==0:
                    set_limit=1;
                    limit_price=current_price
                    can_sell=can_sell+1;

    count=count+1;
    if count>20000000:
        flag=0;
     
plt.plot(tot)        
tot_fin.append(tot[-1])
plt.show()
plt.pause(0.001)
#time.sleep(1-time.time()+current_time+start_time)
    
    
    
        
    

