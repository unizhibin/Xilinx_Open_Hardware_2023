# ----------------------------------------------------------------------------------
# -- Company: University of Stuttgart (IIS)
# -- Engineer: Yichao Peng
# -- 
# -- Description: 
# -- This Python file is for communication with FPGA board (Pynq ZU)
# ----------------------------------------------------------------------------------

import src.all_of_the_parameters as all_of_the_parameters
from pynq import Overlay
import warnings

chip_cfg_data_default = all_of_the_parameters.chip_cfg_data_default
path_to_bitstream = all_of_the_parameters.path_to_bitstream
Dep_Mem = all_of_the_parameters.Dep_Mem
sample_size = all_of_the_parameters.sample_size

warnings.filterwarnings("ignore", message="Setting frequency to the closest possible value") # ignore frequency inaccuracy problem
ol = Overlay(path_to_bitstream)
pulse_gen = ol.fpga_pulse_generator_0    # DACs Pulse Generator unit
osci = ol.fpga_tracing_0    # ADCs tracing unit
adc0 = ol.fpga_ADC_AD7960_0 # ADC drivers
adc1 = ol.fpga_ADC_AD7960_1
chip_cfg = ol.fpga_nmr_chip_config_0 # chip config control unit definition

# dictionary for tracing fpga controlling
fpga_func_dict = all_of_the_parameters.fpga_func_dict

"""
Controlling Functions for nmr chip config
"""

def fpga_func_chip_cfg(input):
    chip_cfg.write(0 * 4, input)  #config data to chip config 
    chip_cfg.write(1 * 4, 1)  #chip config start
    return 


"""
Controlling Functions for tracing part
"""

def enable(input):
    osci.write(fpga_func_dict['C_ENABLE_CMD'],input)
    return

def disable():
    osci.write(fpga_func_dict['C_ENABLE_CMD'],0)
    return

def digtal_trigger_ris_edge(input):#0/1
    osci.write(fpga_func_dict['C_BIN_CH_RE_TRIG_EN_CMD'],input)
    return

def digtal_trigger_fal_edge(input):#0/1
    osci.write(fpga_func_dict['C_BIN_CH_FE_TRIG_EN_CMD'],input)
    return

def set_nr_samples(data):
    osci.write(fpga_func_dict['C_SET_NR_SAMPLES_CMD'],data)
    return
    
def clock_step_size(data):
    osci.write(fpga_func_dict['C_CLOCK_STEP_SIZE_CMD'],data)
    return
    
def trigger_delay(data):
    osci.write(fpga_func_dict['C_SET_TRIGGER_DELAY_CMD'],data)
    return
    
def set_stream_number_rx_pulse(data):
    osci.write(fpga_func_dict['C_SET_STREAM_NR_RX_PULSE'],data)
    return
    
def start_stream_transfer():
    osci.write(fpga_func_dict['C_START_STREAM'],1)
    return

def terminate_stream_transfer():
    osci.write(fpga_func_dict['C_START_STREAM'],0)
    return
    
def type_stream(data):
    osci.write(fpga_func_dict['C_TYPE_STREAM'],data)
    return

def dma_init():
    dma    = ol.axi_dma_0
    dma_send = ol.axi_dma_0.sendchannel
    dma_recv = ol.axi_dma_0.recvchannel
    return dma, dma_send, dma_recv

def fpga_tracing_init(samples):
    
    # ADC configure
    mode = 9
    # 0 = rising , 1 = falling
    adc0.write(0x0,mode)
    adc1.write(0x0,mode)
    
    chip_cfg.write(0 * 4, chip_cfg_data_default)  # config data to chip config
    chip_cfg.write(1 * 4, 1)  # chip config start

    set_nr_samples(samples) # 2**15
    set_stream_number_rx_pulse(1)
    trigger_delay(-2**(Dep_Mem-1)+1)

    clock_step_size(10)
    digtal_trigger_ris_edge(0)
    digtal_trigger_fal_edge(0)
    return
