using frontend.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace frontend.Controllers
{
    public class HomeController : Controller
    {
        public HomeController() { }

        public IActionResult Index()
        {
            return View(new BikeTheftViewModel());
        }

        [HttpPost]
        public async Task<IActionResult> Index(BikeTheftViewModel bikeTheftViewModel)
        {
            using (var client = new HttpClient())
            {
                // api accepts a list, so we'll post data as a list, that only has one item in it

                var list = new dynamic[1];

                // Example input:
                //var mydata = new
                //{
                //    Occurrence_Hour = 5,
                //    Bike_Speed = 30,
                //    Cost_of_Bike = 3000,
                //    Report_Lag = 5,
                //    Primary_Offence_THEFT = 1,
                //};
                //list.Append(mydata);

                list.Append(bikeTheftViewModel);

                var json = JsonConvert.SerializeObject(list);
                var data = new StringContent(json, Encoding.UTF8, "application/json");

                //var url = "https://comp309-group2-flaskapi.azurewebsites.net/predict";
                var url = "http://127.0.0.1:12345/predict";

                var response = await client.PostAsync(url, data);

                if(response.IsSuccessStatusCode)
                {
                    dynamic result = JsonConvert.DeserializeObject(response.Content.ReadAsStringAsync().Result);
                    string returned = result.returned;
                    if(returned.Equals("[0]")) // bike is NOT likely to be returned
                    {
                        ModelState.AddModelError("", "Prediction: Bike is NOT likely to be returned");
                        return View(bikeTheftViewModel);
                    }
                    else // bike is likely to be returned
                    {
                        ModelState.AddModelError("", "Prediction: Bike is likely to be returned");
                        return View(bikeTheftViewModel);
                    }
                }

                ModelState.AddModelError("", "An error occured, please try again.");
                return View(bikeTheftViewModel);
            }
        }
    }
}
