using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using ServiceNet.Models;

namespace ServiceNet.Controllers
{
    public class ServicesController : Controller
    {
        // GET:
        public ActionResult Date([FromQuery(Name = "time")] String time)
        {
            var model = new DateViewModel();
            String check = "?time";
            if (Request.Query.ContainsKey("time"))
            {
                model.ReturnDate = DateTime.Now.ToString("dd.MM.yyyy HH:mm:ss");
            }else if(!Request.QueryString.HasValue) {            
                model.ReturnDate = DateTime.Now.ToString("dd.MM.yyyy");
            }
            else
            {
                model.ReturnDate = "INVALID OPERАTION - the service only functions either without any parameters or with the parameter \"time\", used with or without a value";
            }
            return View(model);
        }

        // GET:
        public ActionResult Calculator([FromQuery(Name = "operand1")] float operand1, [FromQuery(Name = "operation")] String operation, [FromQuery(Name = "operand2")] float operand2)
        {
            var model = new ServiceViewModel();
            String text = "INVALID OPERАTION - parameters \"operand1\" and \"operand2\" are required and should be integer values, \"operation\" is required and the value should be one of: \"plus\", \"minus\", \"multiply - by\", \"divide - by\"";
            if (!Request.Query.ContainsKey("operand1") || !Request.Query.ContainsKey("operand2") || !Request.Query.ContainsKey("operation"))
                { 
                model.text = text;
                return View(model); 
                }
            else
                {                
                model.operand1 = operand1;
                model.operand2 = operand2;
                model.operator1 = operation;
                model.result = 0;
                if (model.operator1 == "plus")
                {
                    model.result = operand1 + operand2;
                }
                if (model.operator1 == "minus")
                {
                    model.result = operand1 - operand2;
                }
                if (model.operator1 == "multiply-by")
                {
                    model.result = operand1 * operand2;
                }
                if (model.operator1 == "divide-by")
                {
                    model.result = operand1 / operand2;
                }
            }
            return View(model);
        }

        
    }
}
