PhotoViewerExpress README
==================

Thank you for checking out the PhotoViewerExpress project.

I first started this project keeping to goals in mind:
 * Get startet and learn a bit of Pyramid web Framework.
 * End up with something I could use in the end to solve
   one problem I had: View all of my pictures I keep in my
   host server (Over 5000 pictures).

To do it, I made the following assumptions:
 * I dont want to have to create albums or galleries to add pictures.
 * I dont want to relie on data stored in DBs for the pictures.
 * They should be showed as they are organized in the filesystem,
   just as if I was using a file browser.
 * I want to keep them in the original size and format (They are there
   because it is a safe place to keep them.)
 * I dont want to generate and store in disk thumbnails and view size files.
 * I dont want everyone see my pictures.
 * I want some people to see some of my pictures.
 * I want some other people to be able to see all my pictures.

Result:
 * A web viewer that requires a login.
 * The logged person can have:
  - public access: It is able to see all pictures under <MyPictures>/public
  - private access: It is able to see all that public can plus <MyPictures>/private
  - admin access: It is able to see public and private and can access the admin page:
   - create/delete users
 * You can see all folders and pictures inside those folder as thumbnails.
 * You can click on thumbnails to see the picture and a pre configured size.
 * All thumbnails and view size pictures are generated in run time, what is 
   more cpu consuming but I dont need to worry about thumbnail and view size
   images storage and sincronization with possible file modifications. What
   you have stored is what you are gonna get.

You can check a live demo at: http://pve-demo.debonzi.com
for public view use: public/public
for private view use: private/private

I hope you enjoy it!
Daniel Debonzi
