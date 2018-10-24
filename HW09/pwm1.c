#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"

volatile register uint32_t __R30;
volatile register uint32_t __R31;

void main(void)
{
	uint32_t gpio;

	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	gpio = 1<<5; // Select which pin to toggle.

	while (1) {
		__R30 |= gpio;
		__delay_cycles(10000);  // This makes it run at about 40MHz for me
		__R30 &= ~gpio;
		__delay_cycles(10000);
	}
}
