import yfinance as yf
import pandas as pd

yf.pdr_override()

#stocklist =['AA','AAL','AAOI','AAPL','ABBV','ABC','ABNB','ABT','ACAD','ACB','ACN','ADBE','ADI','ADM','ADP','ADSK','AEO','AFL','AFRM','AG','AGNC','AIG','ALGN','AMAT','AMBA','AMC','AMD','AMGN','AMLP','AMPX','AMRN','AMRS','AMZN','ANET','ANF','ANY','APA','APO','APPH','APPS','APRN','APT','AR','ARKF','ARKG','ARKK','ASHR','ASML','ASO','ASTS','ATER','ATVI','AUY','AVGO','AVXL','AVYA','AXP','AZN','AZO','BA','BABA','BAC','BAX','BB','BBBY','BBIG','BBWI','BBY','BDX','BHC','BIDU','BIIB','BILI','BILL','BITO','BK','BKKT','BKLN','BKNG','BLK','BLNK','BMY','BNTX','BOIL','BP','BRCC','BRKB','BROS','BTBT','BTU','BUD','BURL','BX','BYND','C','CAG','CAH','CANO','CAR','CAT','CBOE','CC','CCJ','CCL','CEI','CF','CGC','CHPT','CHTR','CHWY','CI','CL','CLAR','CLF','CLOV','CLR','CLVS','CLX','CMCSA','CME','CMG','CNC','CODX','COF','COIN','COOP','COP','COST','COTY','COUP','CPB','CPNG','CPRI','CRM','CRON','CRSP','CRWD','CS','CSCO','CSIQ','CSTM','CSX','CTRA','CVNA','CVS','CVX','CWH','CZR','DAL','DASH','DB','DBX','DD','DDD','DDOG','DE','DFS','DG','DHI','DHR','DIA','DIS','DISH','DJX','DKNG','DKS','DLTR','DNMR','DOCU','DOW','DPZ','DUST','DVN','DWAC','EA','EBAY','EDIT','EDU','EEM','EFA','ELV','EMB','EMR','ENPH','ENVX','EOG','EPD','EQT','ERX','ET','ETSY','EVTL','EW','EWC','EWG','EWU','EWY','EWZ','EXAS','EXPE','EXPR','F','FAS','FAZ','FAZE','FCEL','FCX','FDX','FEZ','FFIE','FFIV','FISV','FIVE','FL','FNHC','FOXA','FSLR','FSLY','FSR','FUBO','FUTU','FXE','FXI','GD','GDX','GDXJ','GE','GETY','GILD','GLD','GLW','GM','GME','GNRC','GNUS','GOEV','GOLD','GOOG','GOOGL','GOOS','GPRO','GPS','GRAB','GRWG','GS','GSAT','GSK','GT','HAL','HBI','HD','HES','HIG','HIMX','HL','HLF','HOG','HON','HOOD','HPQ','HRL','HSBC','HSY','HUM','HUT','HYG','HYMC','IAU','IBB','IBM','ICLN','IEF','ILMN','INFN','INO','INTC','INTU','IP','IQ','IRBT','IRNT','ISRG','ITB','ITW','IVR','IVV','IWM','IYR','JBLU','JD','JDST','JETS','JKS','JMIA','JNJ','JNPR','JNUG','JPM','JWN','KGC','KHC','KKR','KLAC','KMB','KMI','KO','KODK','KR','KRE','KSS','KWEB','LABD','LABU','LAZR','LCID','LEN','LI','LITE','LL','LLY','LMND','LMT','LOW','LQD','LRCX','LULU','LUMN','LUV','LVS','LYFT','M','MA','MAR','MARA','MCD','MCHP','MCK','MDB','MDLZ','MDT','MELI','MET','META','MGM','MJ','MMAT','MMM','MNKD','MNST','MO','MOMO','MOS','MPC','MPW','MRK','MRNA','MRO','MRVL','MS','MSFT','MSOS','MSTR','MT','MTCH','MU','MULN','MVIS','MXEA','MXEF','NCLH','NCR','NEGG','NEM','NEOG','NET','NFLX','NIO','NKE','NKLA','NLY','NNDM','NNOX','NOC','NOK','NOV','NOW','NRGV','NSC','NTAP','NTES','NTR','NUE','NUGT','NVAX','NVDA','NXPI','OCGN','OIH','OKTA','OLED','OLN','ON','OPEN','ORCL','OSTK','OXY','PAA','PACB','PANW','PARA','PBR','PCG','PDD','PENN','PEP','PFE','PG','PGY','PHUN','PINS','PLAY','PLTR','PLUG','PM','PNC','PPG','PRTY','PSFE','PSNY','PSX','PTON','PXD','PYPL','QCOM','QQQ','QS','RACE','RAD','RBLX','RCL','REGN','RH','RIDE','RIG','RIOT','RIVN','RKT','RNG','ROKU','ROOT','ROST','RRC','RTX','RUM','SABR','SARK','SAVA','SAVE','SBLK','SBUX','SCHW','SDC','SDS','SE','SFIX','SHOP','SIG','SILJ','SIRI','SKLZ','SKX','SLB','SLV','SMH','SNAP','SNDL','SNOW','SO','SOFI','SOLO','SONO','SONY','SOXL','SOXS','SPCE','SPGI','SPLK','SPOT','SPWR','SPXL','SPXS','SPXU','SPY','SQ','SQQQ','SRNE','SRPT','SSO','SSYS','STEM','STNE','STX','STZ','SU','SVXY','SWKS','SWN','SYF','SYK','SYY','T','TAL','TAN','TBT','TDOC','TEAM','TECK','TELL','TEVA','TGT','THC','TIP','TJX','TLRY','TLT','TME','TMO','TMUS','TNA','TNDM','TOL','TPR','TQQQ','TRIP','TSCO','TSLA','TSM','TTCF','TTD','TTWO','TWLO','TWTR','TXN','TZA','U','UA','UAA','UAL','UBER','UCO','ULTA','UNG','UNH','UNP','UPRO','UPS','UPST','URA','URBN','URI','USB','USO','UUP','UVIX','UVXY','UWMC','V','VALE','VERU','VFC','VIPS','VIXY','VLO','VRTX','VTRS','VXRT','VXX','VZ','W','WB','WBA','WBD','WDAY','WDC','WE','WEAT','WFC','WHR','WISH','WKHS','WM','WMB','WMT','WOOF','WPM','WW','WY','WYNN','X','XBI','XEO','XHB','XLB','XLC','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY','XME','XOM','XOP','XPEV','XRT','YETI','YINN','YY','Z','ZEN','ZIM','ZM','ZS',]
stocklist =['AA']
optionsX = pd.DataFrame()

for x in stocklist:
    print(x)
    tk = yf.Ticker(x)  
    exps = tk.options  #expiration dates
    try:
        for e in exps:
            print(e)
            opt = tk.option_chain(e)
            print(opt);
            opt = pd.DataFrame().concat(opt.calls).concat(opt.puts)
            
            
            opt['expirationDate'] = e
            opt['Symbol'] = x
            optionsX = optionsX.concat(opt, ignore_index=True)
            
            
            
    except:
        pass
optionsX

