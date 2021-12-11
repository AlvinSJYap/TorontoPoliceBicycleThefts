using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace frontend.Models
{
    public class BikeTheftViewModel
    {
        public string Bike_Model { get; set; }
        public int Bike_Cost { get; set; }
        public string Bike_Colour { get; set; }
        public string Occurence_Date { get; set; }
        public string Primary_Offence { get; set; }
        public string Neighbourhood_Name { get; set; }
        public string Location_Type { get; set; }
    }
}
