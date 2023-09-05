//+------------------------------------------------------------------+
//|                                                      MA_Cross.mq4 |
//|                        Copyright 2023, MetaQuotes Software Corp. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "2023, MetaQuotes Software Corp."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property indicator_separate_window
#property indicator_buffers 2
#property indicator_color1 Lime   // Cor da MA de 6 períodos
#property indicator_color2 Red    // Cor da MA de 21 períodos

// Parâmetros das médias móveis
input int fastMA_Period = 6;     // Período da MA rápida
input int slowMA_Period = 21;    // Período da MA lenta

// Variáveis globais
double maFastBuffer[];
double maSlowBuffer[];
int lastAlertTime = 0;

//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
int OnInit()
  {
   IndicatorBuffers(2);
   SetIndexBuffer(0, maFastBuffer);
   SetIndexBuffer(1, maSlowBuffer);
   SetIndexStyle(0, DRAW_LINE);
   SetIndexStyle(1, DRAW_LINE);
   SetIndexLabel(0, "MA Fast");
   SetIndexLabel(1, "MA Slow");
   
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
  {
   int begin = MathMax(fastMA_Period, slowMA_Period) + 1;
   int crosses = 0;
   
   for (int i = begin; i >= 0; i--)
     {
      maFastBuffer[i] = iMA(NULL, 0, fastMA_Period, 0, MODE_SMA, PRICE_CLOSE, i);
      maSlowBuffer[i] = iMA(NULL, 0, slowMA_Period, 0, MODE_SMA, PRICE_CLOSE, i);
      
      if (i > 0 && maFastBuffer[i] > maSlowBuffer[i] && maFastBuffer[i - 1] <= maSlowBuffer[i - 1])
         crosses++;
      if (i > 0 && maFastBuffer[i] < maSlowBuffer[i] && maFastBuffer[i - 1] >= maSlowBuffer[i - 1])
         crosses++;
     }
   
   if (crosses > 0 && TimeCurrent() - lastAlertTime > 60) // Evita alertas frequentes
     {
      PlaySound("alert.wav");
      lastAlertTime = TimeCurrent();
     }
   
   return(rates_total);
  }
