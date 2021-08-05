package services;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.servlet.http.HttpServletRequest;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Optional;

@SpringBootApplication
@Controller
public class ServicesApplication {

    public static void main(String[] args) {
        SpringApplication.run(ServicesApplication.class, args);
    }

    @GetMapping("/")
    public String Blank(Model model){
        model.addAttribute("view","OK");
        model.addAttribute("title","STATUS");
        return "base-layout";
    }

    @GetMapping("/date")
    public String Date(@RequestParam(value = "time", required = false) Optional<String> time,Model model,HttpServletRequest request) {
        if (time.isPresent()) {
            LocalDateTime myObj = LocalDateTime.now();
            DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd.MM.yyyy HH:mm:ss");
            String Date = myObj.format(myFormatObj);
            model.addAttribute("title","Current Date and Time");
            //boolean verbose = request.getParameterMap().containsKey("v");
            //model.addAttribute("view",String.format("INVALID OPERАTION - the service only functions either without any parameters or with the parameter \"time\", used with or without a value"));
            model.addAttribute("view",String.format("%s", Date));
            return "base-layout";
        } else {
            LocalDate myObj = LocalDate.now();
            DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd.MM.yyyy ");
            String Date = myObj.format(myFormatObj);
            model.addAttribute("title","Current Date");
            //HttpServletRequest request = ServletActionContext.getRequest();
            boolean params = request.getParameterMap().isEmpty();
            if (params)
                model.addAttribute("view",String.format("%s", Date));
            else
                model.addAttribute("view",String.format("INVALID OPERАTION - the service only functions either without any parameters or with the parameter \"time\", used with or without a value"));
            return "base-layout";
        }
    }

    @GetMapping("/calculator")
    public String Calculator(@RequestParam(value = "operand1", required = false) Optional<Float> operand1,
                             @RequestParam(value = "operand2", required = false) Optional<Float> operand2,
                             @RequestParam(value = "operation", required = false) Optional<String> operation,
                             Model model
    ) {
        model.addAttribute("title","Calculator");
        float result = 0;
        boolean error = false;
        if (operation.isEmpty() || operand1.isEmpty() || operand2.isEmpty())
            error = true;
        else
            switch (operation.get().toLowerCase(Locale.ROOT)) {
            case "plus":
                result = operand1.get().floatValue() + operand2.get().floatValue();
                break;
            case "minus":
                result = operand1.get().floatValue() - operand2.get().floatValue();
                break;
            case "multiply-by":
                result = operand1.get().floatValue() * operand2.get().floatValue();
                break;
            case "divide-by":
                result = operand1.get().floatValue() / operand2.get().floatValue();
                break;
            default:
                error = true;
            };
        if (error)
            model.addAttribute("view",String.format("INVALID OPERАTION - parameters \"operand1\" and \"operand2\" are required and should be integer values, \"operation\" is required and the value should be one of: \"plus\", \"minus\", \"multiply-by\", \"divide-by\""));
        else
            model.addAttribute("view",String.format("%.0f %s %.0f -> %.0f" , operand1.get().floatValue(),operation.get().toLowerCase(Locale.ROOT),operand2.get().floatValue(),result));
        return "base-layout";
    }
}
