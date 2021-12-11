using frontend.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
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
        public HomeController()
        {

        }

        public IActionResult Index()
        {
            return View(new BikeTheftViewModel());
        }

        [HttpPost]
        public async void Index(BikeTheftViewModel bikeTheftViewModel)
        {
            using (var client = new HttpClient())
            {
                var json = JsonConvert.SerializeObject(bikeTheftViewModel);
                var data = new StringContent(json, Encoding.UTF8, "application/json");

                var url = "https://comp309-group2-flaskapi.azurewebsites.net/predict";

                var response = await client.PostAsync(url, data);

                string result = response.Content.ReadAsStringAsync().Result;
            }
        }
    }
}
