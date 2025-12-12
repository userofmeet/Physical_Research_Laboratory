#include <avr/io.h>
#include <util/delay.h>
#include <math.h>

#define VREF 2.56            
#define VEX 2.56             
#define GAIN 5.0             
#define R_FIXED 1000.0       
#define TEMP_SETPOINT 25.0   
#define HYSTERESIS 1.0       

void ADC_init(void)
{
	ADMUX = (1 << REFS1) | (1 << REFS0); // internal 2.56V 
	ADCSRA = (1 << ADEN) |
	(1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0); // Prescaler 128
}

uint16_t ADC_read(uint8_t channel)
{
	ADMUX = (ADMUX & 0xE0) | (channel & 0x07); // select channel
	ADCSRA |= (1 << ADSC);                     // start conversion
	while (ADCSRA & (1 << ADSC));              // wait
	return ADCW;
}

double ADC_to_voltage(uint16_t adc_val)
{
	return ((double)adc_val * VREF) / 1023.0;
}

double voltage_to_RTD(double V_adc)
{
	double V_diff = V_adc / GAIN; // remove gain effect
	if (V_diff <= 0) return -1;   // error check
	double R_pt = R_FIXED * (V_diff / (VEX - V_diff));
	return R_pt;
}
double RTD_to_temp(double R_pt)
{
	return (R_pt - 1000.0) / 3.85; 
}

 main(void)
{
	ADC_init();
	while (1)
	{
		uint16_t raw = ADC_read(0); // ADC0
		double V_adc = ADC_to_voltage(raw);
		double R_pt = voltage_to_RTD(V_adc);
		double T = RTD_to_temp(R_pt);
		_delay_ms(1000); 
	}
}
