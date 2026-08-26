// #include <cairo.h>

// int main()
// {
//     cairo_surface_t *surface =
//         cairo_image_surface_create(CAIRO_FORMAT_ARGB32,400,300);

//     cairo_t *cr = cairo_create(surface);

//     cairo_rectangle(cr,50,50,200,100);
//     cairo_stroke(cr);

//     cairo_arc(cr,300,150,40,0,2*3.14);
//     cairo_stroke(cr);

//     cairo_move_to(cr,100,250);
//     cairo_show_text(cr,"Hello Cairo");

//     cairo_surface_write_to_png(surface,"output.png");

//     cairo_destroy(cr);
//     cairo_surface_destroy(surface);

//     return 0;
// }