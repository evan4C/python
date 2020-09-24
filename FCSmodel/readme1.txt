******************************************************************************************
COPYRIGHT  © 2002 
THE REGENTS OF THE UNIVERSITY OF MICHIGAN
ALL RIGHTS RESERVED

PERMISSION IS GRANTED TO USE, COPY AND REDISTRIBUTE THIS SOFTWARE FOR NONCOMMERCIAL EDUCATION AND RESEARCH PURPOSES, SO LONG AS NO FEE IS CHARGED, AND SO LONG AS THE COPYRIGHT NOTICE ABOVE, THIS GRANT OF PERMISSION, AND THE DISCLAIMER BELOW APPEAR IN ALL COPIES MADE; AND SO LONG AS THE NAME OF THE UNIVERSITY OF MICHIGAN IS NOT USED IN ANY ADVERTISING OR PUBLICITY PERTAINING TO THE USE OR DISTRIBUTION OF THIS SOFTWARE WITHOUT SPECIFIC, WRITTEN PRIOR AUTHORIZATION.  PERMISSION TO MODIFY OR OTHERWISE CREATE DERIVATIVE WORKS OF THIS SOFTWARE IS NOT GRANTED.

THIS USE OF THIS SOFTWARE REQUIRES SIMULINKÒ, A LICENSED PRODUCT OF THE MATHWORKS, INC.  THE SOFTWARE USER IS SOLELY RESOPNSIBLE FOR OBTAINTING AN APPROPRIATE LICENSE FOR SIMULINKÒ.  NO LICENSE TO SIMULINKÒ IS GRANTED, INFERRED OR IMPLIED BY THE DISTRIBUTION OF THIS SOFTWARE.

THIS SOFTWARE IS PROVIDED AS IS, WITHOUT REPRESENTATION AS TO ITS FITNESS FOR ANY PURPOSE, AND WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE REGENTS OF THE UNIVERSITY OF MICHIGAN SHALL NOT BE LIABLE FOR ANY DAMAGES, INCLUDING SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, WITH RESPECT TO ANY CLAIM ARISING OUT OF OR IN CONNECTION WITH THE USE OF THE SOFTWARE, EVEN IF IT HAS BEEN OR IS HEREAFTER ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
******************************************************************************************

** Platform
The model is created in Simulink 5 (R13) but is saved as Simulink 4 (R12). Therefore, it should work fine with Simulink 4 (R12).

** To run the model
- run fcsmain.m (load model parameters and open the simulink model)
- run the simulink model
- run fcsplot.m (plot some variables)
- output variables are exported to Matlab workspace with name starting with 'out'. Use command 'who out*' to get the list. 

** Description of files and folders
fpsmain.m - main m-file
fpsplot.m - m-file for plotting simulation results
readme.m - this file
\data\ - folder contains model parameters
\setpoints\ - folder contains initial values of model inputs and states at different net power (23,30,35,40,45,50 kW)

** The model is created by
Jay Tawee Pukrushpan, Anna Stefanopoulou, and Huei Peng
Fuel Cell Control Systems Laboratory (FCCS)
Department of Mechanical Engineering
University of Michigan

** Model derivation
The detail of the model can be found in
Control of Fuel Cell Power Systems: Principles, Modeling, Analysis and Feedback Design
by J.T. Pukrushpan, A.G. Stefanopoulou, H. Peng
Series : Advances in Industrial Control
ISBN: 1-85233-816-4
 
** Special note: 
Unlike in the thesis, in the model, x represents mole fraction and y represents mass fraction.
