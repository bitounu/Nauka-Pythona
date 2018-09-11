import imgui

# start new frame context
imgui.new_frame()

# open new window context
imgui.begin("Your first window!", True)

# draw text label inside of current window
imgui.text("Hello world!")

# close current window context
imgui.end()

# pass all drawing comands to the rendering pipeline
# and close frame context
imgui.render()
