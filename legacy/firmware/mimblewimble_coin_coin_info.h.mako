// This file is automatically generated from mimblewimble_coin_coin_info.h.mako
// DO NOT EDIT

// Header guard
#ifndef __MIMBLEWIMBLE_COIN_COIN_INFO_H__
#define __MIMBLEWIMBLE_COIN_COIN_INFO_H__


// Header files
#include "mimblewimble_coin_coins.h"


// Definitions

// Coins count
<% mimblewimble_coin_coins_list = list(supported_on("trezor1", mimblewimble_coin)) %>\
#define MIMBLEWIMBLE_COIN_COINS_COUNT ${len(mimblewimble_coin_coins_list)}


// Constants

// Coins
extern const MimbleWimbleCoinCoinInfo mimbleWimbleCoinCoins[MIMBLEWIMBLE_COIN_COINS_COUNT];


#endif
