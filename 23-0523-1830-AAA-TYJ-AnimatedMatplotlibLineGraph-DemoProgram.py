#!/usr/bin/env python
import PySimpleGUI as sg

from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def main():

    ###jwc o NUM_DATAPOINTS = 10000
    NUM_DATAPOINTS = 10000
    # define the form layout
    layout = [[sg.Text('Animated Matplotlib', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Canvas(size=(640, 480), key='-CANVAS-')],
              [sg.Text('Progress through the data')],
              [sg.Slider(range=(0, NUM_DATAPOINTS), size=(60, 10), orientation='h', key='-SLIDER-')],
              [sg.Text('Number of data points to display on screen')],
               [sg.Slider(range=(10, 500), default_value=40, size=(40, 10), orientation='h', key='-SLIDER-DATAPOINTS-')],
              [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14')]]

    # create the form and show it without the plot
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout, finalize=True)

    canvas_elem = window['-CANVAS-']
    slider_elem = window['-SLIDER-']
    canvas = canvas_elem.TKCanvas

    # draw the initial plot in the window
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
    fig_agg = draw_figure(canvas, fig)
    # make a bunch of random data points
    dpts = [randint(0, 10) for x in range(NUM_DATAPOINTS)]

    for i in range(len(dpts)):
        event, values = window.read(timeout=0)   # WARNING! timeout=0 will chew up 100% of your CPU
        if event in ('Exit', None):
            exit(69)
        slider_elem.Update(i)       # slider shows "progress" through the data points
        ax.cla()                    # clear the subplot
        ax.grid()                   # draw the grid
        data_points = int(values['-SLIDER-DATAPOINTS-']) # draw this many data points (on next line)
        ax.plot(range(data_points), dpts[i:i+data_points],  color='purple')
        fig_agg.draw()


if __name__ == '__main__':
    sg.change_look_and_feel('Dark')
    main()
