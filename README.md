Bulletproof, A Filament Dryer for 3d printing.

After burning through my third filament dryer, I got fed up with the layers of planned obsolescence baked into cheap products (and expensive products with cheap COTS parts).

I want my filament dryer to just work, no fuss, just do it's job so I can focus on printer bits.

So I built this relatively quickly.
*This is not a maintained project*, I do not plan to build more of this any time soon.  Depending on what parts are available to you, this exact build could prove prohibitively expensive.

This is not an MMU/AMS type system, it's just a very beefy, and has features I want. 

I'm posting this as open source for inspiration, but if you build it exactly, well that's awesome! 
If it inspires your build, I'd love to hear about it!  <unixcardbide@blackhole.lol>

--
Dehydrator Requirements (based on my experiences):

- Dehydrate filament for most "common" filaments.
- Feed directly into printer (like many products/designs do).

- Dehydrate via heat, as this becomes a side-feature, providing excellent consistency for filament entering the printer.  When filament temps are deterministic entering the printer, print repeatability and fine settings are enhanced.
- Dual roller-bar designs are super common, they've been most stable for me.

- Keep the hot parts mechanically governed:
- I'm using a single 150w Silicone-Pad type heater, 110v, with an internal temperature regulator that runs around 195C.  These can operate as safely as incandescant light bulbs, but in a form factor more useful to this application.
- I'm using a single adjustable 110v thermostat, which maxes out at 85C, designed for equipment which is intended to operate somewhere "below boiling point".
- For double safety, (heat!), I added an extra "peak heat" safety thermostat, open circuit until 95C, (a thermostatic fuse would work as well here).

- A scrap Aluminum heat sink (ebay) is what the silicone pad heater is attached to, which is an ideal way to radiate the heat to the air inside the box.  However, just a suficcient piece of aluminum sheet would also radiate heat very well, as would other metals which have good conductive properties.  This is similar to any heated print-bed in a common 3d printer, which is your best source of chamber heat!

A note on PTC heaters, (I'm not using one here), here's why I stay away from them in general
My experiences with PTC heaters for 3d printing chamber air applications has not been great, I find they pose several problems which are difficult or dangerous to overcome:
- PTC heaters immediately blow jets of very hot air, (by design), and I find it difficult/constraining to design things in a way where those jets don't create hot spots in the chamber, or on whatever they get pointed at.  Good PTC heater design requires large open spaces in the chamber being heated.
- For printer enclosures, PTC heaters move a lot of air quickly, which often creates other problems for the prints.
- For "uniform chamber air temp" applications, PTC heaters can consume more electricity than radiant methods, (depending on design).
- PTC heaters have numerous moving parts, and are more prone to failure.
- Inexpensive PTC heaters are common, but these are very prone to failure, and PTC failure commonly means meltdowns or actual fire.


I want to be able to power off the enclosure but leave filament inside for days/weeks, so,
- Metal Enclosure, (used an Ammo can).  Plastic is hygroscopic.  The only "leaky" place in this design is the PTFE/Bowden tube where the filament exits the case, which, when filled with filament, is a very tiny opening for humidity to leak in.
- Solenoid valves for the "breather holes".  When heat is on, humidity needs a place to escape.  Most dryboxes have multiple holes high and low, to allow this.  When power is cut to the heat, metal solenoid valves close, preventing humidity from rushing back into the box.

I want to accurately measure the RH and temp in the filament chamber.  While RH measurements below 15% are nontrivial, the SHT series chips from Sensirion are basically the standard here.
https://sensirion.com/products/catalog/SHT45
Adafruit produces some easy to use (and Klipper friendly) i2c boards,
https://www.adafruit.com/product/5665

For this build, I'll be using an ESP32 based "Featherboard" with TFT display.
https://circuitpython.org/board/adafruit_feather_esp32s3_reverse_tft/
I'll be wiring up UART/Serial, so I can read the RH/Temp values from Klipper/Kalico based host machines (via actual serial, or USB-serial adapter).

And, if Klipper can read the RH/Temps, I certainly want the ability for Klipper to turn the heater on or off.  I *do not* need or want to control the temperature via Klipper, (that's simple enough to set on the dial according to the filament being loaded, when one is touching the box loading it).
I do however, want to be able to write macros that do things like: "if the RH of the filament chamber is above (N)%, pause before heat-soak/warmup/printing, turn on the filament chamber heat, and wait until the RH in the chamber has been below (x)% for (y)hrs before starting the print..." 
This may not be the design you want, but it's absolutely the design I want.

---
Quirks

- To power the ESP32/featherboard, USBC is best, (5v).  I recycled an old Apple USB power supply to do this one job.
- All hardware except the featherboard is 110v.  While this eliminates any need for a transformer, as tradeoff, some hardware is a bit clunky or uncommon. (e.g. the 110v fans, or solenoids).
- VERY FEW printed parts are inside the heated chamber, these parts I printed using ASA.  Everything outside the chamber can be any filament you wish, I used PLA+.

---
---
Files included in this repo:

- Original 3d files (I used SketchUp, which is trivially import-able into Fusion360).
- Ammo case specifications and drawings for the case I used.
- STL files for all the printed parts, (labeled as internal or external) 
- CircuitPython code which I'm running on the Featherboard https://learn.adafruit.com/esp32-s3-reverse-tft-feather/overview
- Complete BOM as CSV (with part urls/sources for all but the most common components)


